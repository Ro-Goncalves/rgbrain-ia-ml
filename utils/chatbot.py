from langchain.embeddings.openai import OpenAIEmbeddings
from langchain_community.embeddings import HuggingFaceInstructEmbeddings
from langchain.vectorstores.faiss import FAISS
from langchain.chat_models.openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains.conversational_retrieval.base import ConversationalRetrievalChain
from langchain_community.llms import HuggingFaceEndpoint


def create_vectorstore(chunks):
    """
    ricardo-filho/bert-base-portuguese-cased-nli-assin-2
    WhereIsAI/UAE-Large-V1
    """
    # embeddings = OpenAIEmbeddings()
    embeddings = HuggingFaceInstructEmbeddings(       
        model_name='ricardo-filho/bert-base-portuguese-cased-nli-assin-2'
    )
    vactorstrore = FAISS.from_texts(texts=chunks, embedding=embeddings)
    
    return vactorstrore

def create_conversation_chain(vectorstore):
    """
    google/gemma-7b
    meta-llama/Llama-2-7b-chat-hf
    mistralai/Mixtral-8x7B-Instruct-v0.1
    """
    # llm = ChatOpenAI()
    llm = HuggingFaceEndpoint(
        repo_id='mistralai/Mixtral-8x7B-Instruct-v0.1',
        huggingfacehub_api_token='', 
        temperature=0.5,
        model_kwargs={'max_length':512})
    
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    
    return conversation_chain