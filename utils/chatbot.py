from langchain.embeddings.openai import OpenAIEmbeddings
from langchain_community.embeddings import HuggingFaceInstructEmbeddings
from langchain.vectorstores.faiss import FAISS
from langchain.chat_models.openai import ChatOpenAI
from langchain.memory import ConversationBufferMemory, ConversationSummaryMemory
from langchain.chains.conversational_retrieval.base import ConversationalRetrievalChain
from langchain_community.llms import HuggingFaceEndpoint
from langchain.prompts.prompt import PromptTemplate


def create_vectorstore(chunks):
    """
    ricardo-filho/bert-base-portuguese-cased-nli-assin-2
    WhereIsAI/UAE-Large-V1
    """
    # embeddings = OpenAIEmbeddings()
    # embeddings = HuggingFaceInstructEmbeddings(       
    #     model_name='ricardo-filho/bert-base-portuguese-cased-nli-assin-2'
    # )
    # new_vectorstrore = FAISS.from_texts(texts=chunks, embedding=embeddings)
    
    # vectorstrore = FAISS.load_local('faiss_default', embeddings)
    # vectorstrore.merge_from(new_vectorstrore)

    embeddings = HuggingFaceInstructEmbeddings(       
        model_name='ricardo-filho/bert-base-portuguese-cased-nli-assin-2'
    )
    vactorstrore = FAISS.from_texts(texts=chunks, embedding=embeddings)
    
    return vactorstrore


def create_conversation_chain(vectorstore=None):
    """
    google/gemma-7b
    meta-llama/Llama-2-7b-chat-hf
    mistralai/Mixtral-8x7B-Instruct-v0.1
    """
    # llm = ChatOpenAI()   
    
    if not vectorstore:
        embeddings = HuggingFaceInstructEmbeddings(       
            model_name='ricardo-filho/bert-base-portuguese-cased-nli-assin-2'
        )
        vectorstore = FAISS.load_local('faiss_default', embeddings)
    
    template = """
        Você é um robô chamado Brian, seu objetivo é responder perguntas sobre consórcio de um forma cordial.
        Seja muito respeitoso e sempre use um português polido.

        Conversa atual:
              
        _bot:
    """

    PROMPT = PromptTemplate(input_variables=None, template=template)

    llm = HuggingFaceEndpoint(
        repo_id='mistralai/Mixtral-8x7B-Instruct-v0.1',
        huggingfacehub_api_token='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', 
        temperature=0.5,
        model_kwargs={'max_length':512})
    
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    
    conversation_chain = ConversationalRetrievalChain.from_llm(
        combine_docs_chain_kwargs={'prompt': PROMPT},
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    
    return conversation_chain