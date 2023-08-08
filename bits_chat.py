import os
import streamlit as st

from langchain.llms import OpenAI
from langchain.agents import Tool
from langchain.agents import AgentType, initialize_agent, load_tools
from langchain.callbacks import StreamlitCallbackHandler
from langchain.chains.conversation.memory import ConversationBufferMemory

from llama_index import StorageContext, load_index_from_storage

# styling
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

local_css("style.css")

project_path = "./bioe80"
storage_path = project_path+"/storage"

if os.path.isfile(project_path+"/storage/index_store.json") == False :
    print("Please generate an index first, or check the path")
    quit()

@st.cache_resource
def load_index():
    # rebuild storage context
    storage_context = StorageContext.from_defaults(persist_dir=storage_path)
    # load index
    index = load_index_from_storage(storage_context)
    return index

data_load_state = st.text('Loading BITS index...')
index = load_index()
data_load_state.text("Ready...")

st.title('BITS-BioE80 ')
st.write('Hello, I\'m BITS. I\'m still learning but I\'ve been trained on ~1000 source materials including all BioE80 lectures.')

st.subheader('Example Prompts:')
st.write("What does Drew mean by abstraction?")
st.write("What are the steps to make a probiotic for an endangered frog species?")

input_container = st.container()

# generate BITS from stored vector index
tools = [
    Tool(
        name="BITS",
        func=lambda q: str(index.as_query_engine().query(q)),
        description="useful for when you want to answer questions about BioE80. The input to this tool should be a complete english sentence.",
        return_direct=True,
    ),
]

memory = ConversationBufferMemory(memory_key="chat_history")

#llm = ChatOpenAI(temperature=0, max_tokens=512, model_name="gpt-3.5-turbo") # gpt-4
llm = OpenAI(temperature=0.1, max_tokens=512, streaming=True)

# agent = initialize_agent(tools, llm, agent=AgentType.CONVERSATIONAL_REACT_DESCRIPTION, memory=memory, verbose=True)
agent = initialize_agent(tools, llm, agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION, memory=memory, verbose=True)

if prompt := input_container.chat_input("Ask BITS..."):
    input_container.chat_message("student").write(prompt)
    with input_container.chat_message("BITS"):
        st_callback = StreamlitCallbackHandler(input_container.container())
        response = agent.run(prompt, callbacks=[st_callback])
        input_container.write(response)