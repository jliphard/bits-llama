import os
import streamlit as st
import sys

print(sys.path)

from langchain.llms import OpenAI
from langchain.agents import Tool
from langchain.agents import AgentType, initialize_agent, load_tools
from langchain.callbacks import StreamlitCallbackHandler
from langchain.chains.conversation.memory import ConversationBufferMemory

from llama-index import StorageContext, load_index_from_storage

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def remote_css(url):
    st.markdown(f'<link href="{url}" rel="stylesheet">', unsafe_allow_html=True)    

def icon(icon_name):
    st.markdown(f'<i class="material-icons">{icon_name}</i>', unsafe_allow_html=True)

local_css("style.css")
remote_css('https://fonts.googleapis.com/icon?family=Material+Icons')

project_path = "./bioe80"
storage_path = project_path+"/storage"

if os.path.isfile(project_path+"/storage/index_store.json") == False :
    print("Please generate an index first, or check the path")
    quit()

st.title('BITS-BioE80 ')
st.write('Welcome to BioE80. BITS is still learning but BITS has been trained on all course and lecture materials.')

@st.cache_resource
def load_index():
    # rebuild storage context
    storage_context = StorageContext.from_defaults(persist_dir=storage_path)
    # load index
    index = load_index_from_storage(storage_context)
    return index

data_load_state = st.text('Loading BITS index...')
index = load_index()
print(index)
data_load_state.text("Loading BITS index - done! (using st.cache_index)")

# if st.checkbox('Show Index'):
#     st.subheader('Index')
#     st.write(index)

st.subheader('Example Prompts:')
st.write("What does Drew mean by abstraction?")
st.write("What are the steps to make a probiotic for an endangered frog species")

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

if prompt := st.chat_input("Ask BITS..."):
    st.chat_message("student").write(prompt)
    with st.chat_message("BITS"):
        st_callback = StreamlitCallbackHandler(st.container())
        response = agent.run(prompt, callbacks=[st_callback])
        st.write(response)
