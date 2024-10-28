import os
import streamlit as st
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq  
from langchain_community.utilities import ArxivAPIWrapper, WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun, WikipediaQueryRun, DuckDuckGoSearchRun
from langchain.agents import initialize_agent, AgentType
from langchain.callbacks import StreamlitCallbackHandler

# Load environment variables (if needed)
load_dotenv()

# Initializing the Tools
arxiv_wrapper = ArxivAPIWrapper(top_k_results=1, doc_content_chars_max=200)
arxiv = ArxivQueryRun(api_wrapper=arxiv_wrapper)

api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=200)
wiki = WikipediaQueryRun(api_wrapper=api_wrapper)

search = DuckDuckGoSearchRun(name='search')

# Streamlit UI setup
st.title("Langchain - Search Engine")
st.markdown("""
In this example, we are using the 'StreamlitCallbackHandler' to display the thought and actions of an agent in an interactive Streamlit app.
Try more Streamlit Agent examples at [GitHub].
""")

# Sidebar for Groq API-KEY
st.sidebar.title("Settings")
api_key = st.sidebar.text_input("Enter your Groq API-Key:", type="password")
if st.sidebar.button("Submit API Key"):
    if api_key:
        st.sidebar.success("API Key submitted successfully!")
    else:
        st.sidebar.error("Please enter a valid API Key.")


# Initialize session state for messages
if "messages" not in st.session_state:
    st.session_state["messages"] = [
        {"role": "assistant", "content": "Hi, I am a chatbot who can search for you. How can I help you?"}
    ]

# Display previous messages
for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg['content'])

# User input and processing
if prompt := st.chat_input("What would you like to search for?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    llm = ChatGroq(groq_api_key=api_key, model_name="Llama3-8b-8192", streaming=True)
    tools = [search, arxiv, wiki]

    search_agent = initialize_agent(tools, llm, AgentType.ZERO_SHOT_REACT_DESCRIPTION, handling_parsing_errors=True)

    with st.chat_message('assistant'):
        st_cb = StreamlitCallbackHandler(st.container(), expand_new_thoughts=False)
        try:
            response = search_agent.run(st.session_state.messages, callbacks=[st_cb])
            st.session_state.messages.append({"role": "assistant", "content": response})
            st.write("### Response:")
            st.write(response)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            st.session_state.messages.append({"role": "assistant", "content": "Sorry, I encountered an error while processing your request."})

# Add a footer for additional information# Add a footer with emojis for Langchain and Streamlit
st.markdown("---")
st.markdown("Made with 🛠️ Langchain and 📊 Streamlit")
