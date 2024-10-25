import os
import streamlit as st
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_groq import ChatGroq  
from langchain_community.utilities import ArxivAPIWrapper,WikipediaAPIWrapper
from langchain_community.tools import ArxivQueryRun,WikipediaQueryRun,DuckDuckGoSearchRun
from langchain.agents import initialize_agent ,AgentType
from langchain.callbacks import StreamlitCallbackHandler

# Load environment variables
load_dotenv()
os.environ["HF-TOKEN"] = os.getenv("HF-TOKEN")
api_key = os.environ["GROQ-TOKEN"] = os.getenv("GROQ-TOKEN")

# Initializing the Tools
arxiv_wrapper = ArxivAPIWrapper(top_k_results = 1 , doc_content_chars_max=200)
arxiv = ArxivQueryRun(api_wrapper = arxiv_wrapper)

api_wrapper = WikipediaAPIWrapper(top_k_results=1 , doc_content_chars_max = 200)
wiki = WikipediaQueryRun(api_wrapper=api_wrapper)

search = DuckDuckGoSearchRun(name = 'search')

st.title("lamgchain - SearcH Engine")

"""
In this example, we are using the 'StreamlitCallBackHandler' to display the thought and actions of an agent in an interactive Streamlit app.
Try more streamlit Agent examples at [github.com/langchain-ai/streamlit-agent]

"""
if "messages" not in st.session_state:
    st.session_state["messages"]=[
        {"role":"assistant","content":"HI, I am chatbot who can search for you, How can I help you"}


    ]

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg['content'])

if prompt:=st.chat_input("What is Langchain"):
    st.session_state.messages.append({"role":"user", "content":prompt})
    st.chat_message("user").write(prompt)

    llm = ChatGroq(groq_api_key = api_key , model_name = "Llama3-8b-8192",streaming = True)
    tools = [search,arxiv,wiki]

    search_agent = initialize_agent(tools,llm,AgentType.ZERO_SHOT_REACT_DESCRIPTION , handling_parsing_errors =True)

    with st.chat_message('assistant'):
        st_cb = StreamlitCallbackHandler(st.container(),expand_new_thoughts=False)
        response = search_agent.run(st.session_state.messages, callbacks=[st_cb])
        st.session_state.messages.append({"role":"assistant","content":response})
        st.write(response)
