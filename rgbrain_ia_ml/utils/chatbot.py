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
    sentence-transformers/all-MiniLM-L6-v2
    """   

    embeddings = HuggingFaceInstructEmbeddings(       
        model_name='sentence-transformers/all-MiniLM-L6-v2'
    )
    vactorstrore = FAISS.from_texts(texts=chunks, embedding=embeddings)
    
    return vactorstrore


def create_conversation_chain(vectorstore=None):
    
    template = """Use as seguintes partes do contexto para responder à pergunta no final. Se você não sabe a resposta,
    apenas diga que você não sabe, não tente inventar uma resposta, não responda nada que não seja um texto, 
    você deve seguir as seguintes REGRAS:

    - **RESPONDA SOMENTE EM PORTUGUÊS BRASILEIRO**
    - **SEU NOME É BRAIAN**
    - **VOCÊ É UM ROBÔ ASSISTENTE QUE TIRA AS DÚVIDAS SOBRE CONSORCIO**
    - **SEJA O MAIS CORTÊS POSSÍVEL**
    - **SUAS RESPOSTAS DEVEM CONTER SOMENTE TEXTO**
    
    {context}
    
    Pergunta: {question}
    Resposta em Português Brasileiro:"""

    PROMPT = PromptTemplate(input_variables=['context', 'chat_history'], template=template)

    llm = HuggingFaceEndpoint(
        repo_id='mistralai/Mixtral-8x7B-Instruct-v0.1',      
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