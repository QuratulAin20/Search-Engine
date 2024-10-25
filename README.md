# AI-Powered Search Engine with LangChain and Groq Integration
![Information Retrieval System](https://pfst.cf2.poecdn.net/base/image/0890c2059a1a8bb9edd32894aa6732054906d577a2460d0b4ed2adf3446ee4d3?w=1024&h=1024&pmaid=187754509)


This project presents an AI-powered search engine developed using Streamlit, LangChain, and Groq to enhance information retrieval and interaction. Leveraging the LangChain framework for retrieval-augmented generation (RAG) and integrating Groq-powered LLM capabilities, the application dynamically pulls information from multiple online sources, including Arxiv, Wikipedia, and DuckDuckGo. The search engine can interpret 
user queries, retrieve real-time information, and respond interactively. The system pulls and processes content in response to user queries, effectively creating a “live dataset” from these sources for each session.

The methodology used in this project is the retrieval of information from live resources that use of LangChain for retrieval, and the integration with Groq for enhanced functionality.
- Arxiv: A free distribution service and an open-access archive for scholarly articles.
- Wikipedia: A free, web-based, collaborative, multilingual encyclopedia project.
- DuckDuckGo: A privacy-focused search engine that emphasizes user confidentiality and data protection 

The key components and processes involved in developing an AI-powered search engine application:

1. **Tool and API Initialization**: The application utilizes LangChain to integrate various tools (Arxiv, Wikipedia, DuckDuckGo) with optimized parameters for effective information retrieval.

2. **Language Model Setup**: Groq's LLM ("Llama3-8b-8192") is employed for enhanced language understanding, enabling zero-shot reasoning for intelligent response generation.

3. **Streamlit for User Interaction**: A user-friendly interface is created using Streamlit, allowing real-time interaction with the chatbot and maintaining conversational context through `session_state`.

4. **Callback Integration for Response Transparency**: The `StreamlitCallbackHandler` displays the agent's reasoning steps, providing users with insight into the generation of responses.

5. **Search Query Execution**: The LangChain agent interprets user queries and executes searches across the relevant tools to compile synthesized responses.

6. **Response Handling and Display**: Responses are presented in Streamlit, preserving previous interactions for context-awareness.

7. **Scalability and Customizability**: The modular framework allows for easy addition of new tools, enhancing the application’s adaptability for diverse knowledge retrieval needs.

This methodology provides a structured approach to integrating LLM-driven responses with real-time information retrieval, resulting in a powerful and interactive user experience.

- It enhanced search relevance by the integration of Arxiv, Wikipedia, and DuckDuckGo APIs allows the search engine to retrieve real-time information on a wide range of topics.

-  By utilizing Groq-powered LLM capabilities, the chatbot provides context-aware responses that retain the flow of conversation across multiple queries.

- The use of the StreamlitCallbackHandler allows users to view the chatbot’s reasoning steps and intermediate actions in real-time. This feature increases user trust in the system by providing a transparent view of how the chatbot retrieves and selects information.

- The modular design, based on LangChain, ensures that additional data sources or tools can be easily integrated. This adaptability allows the search engine to grow in scope and stay current with new information sources or user needs, indicating a scalable solution for future expansion.

# Further Advancement
By adding embedding along with pdf uploader we can enable semantic search, where users can retrieve relevant information based on meaning rather than specific wording. This is especially helpful for long or technical documents, like research papers or manuals, where synonyms or similar phrases are used throughout.
