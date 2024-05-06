import streamlit as st
from utils import text
from langchain_community.llms import HuggingFaceEndpoint
from langchain_core.prompts.prompt import PromptTemplate
from langchain.chains.llm import LLMChain

st.set_page_config(
    page_title = "Extrair Informações PDF",
    page_icon = "📈"
)

def _model():
    return 'mistralai/Mixtral-8x7B-Instruct-v0.1'

def _llm():    
    return HuggingFaceEndpoint(
        repo_id=_model(),
        huggingfacehub_api_token='', 
        temperature=0.5,
        model_kwargs={'max_length':512})

def _template():   
    return """
        Você está lendo um documento que possui informações sobre consorcio.
        Seu objetivo é extrair as de grupo, cota, código do bem ojeto atual,
        valor do bem objeto atual, código do bem objeto novo, valor do bem objeto
        novo, extraia somente os número, utili

        - **Grupo**:
        - **Cota**:
        - **Código Bem Objeto atual**:
        - **Valor Bem Objeto atual**:
        - **Código Bem Objeto Novo**:
        - **Valor Bem Objeto Novo**:

        ```{text}```
    """

def _llm_chain():
    prompt = PromptTemplate(template=_template(), input_variables=['text'])
    return LLMChain(prompt=prompt, llm=_llm())

LLM_CHAIN = _llm_chain()

if ('texto_pdf' not in st.session_state):
    st.session_state.texto_pdf = None

st.markdown("""
    # Vamos Ver o que  há no seu PDF? 🤔
    ---
            
    Essa demo extraí informações de um PDF
""")

with st.sidebar:
    pdf_docs = st.file_uploader('Dê-Me seu PDF', accept_multiple_files=True)

    if st.button('Processar'):       
        st.session_state.texto_pdf = text.process_files(pdf_docs)

st.markdown(f"""
    ## Contéudo do PDF
    ---
            
    {LLM_CHAIN.invoke(st.session_state.texto_pdf)['text']}
""")