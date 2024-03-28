import streamlit as st
from langchain_community.llms.huggingface_pipeline import HuggingFacePipeline
from transformers import AutoTokenizer
import transformers
import torch

def _auto_tokenizer():
    model = 'lxyuan/distilbert-base-multilingual-cased-sentiments-student'
    return  AutoTokenizer.from_pretrained(model)

def _pipeline():
    

st.set_page_config(
    page_title = "Análise Sentimento",
    page_icon = "📈"
)

st.markdown("""
    # Como Você Está Se Sentindo Hoje
    ---
            
    Essa é uma demo que demonstra como o ***Zero Shot Classification*** funciona. Tentaremos 
    extrair os apspectios e o sentimento sobre ele.    
""")

st.session_state.texto = st.text_input('Diga-Me o que sente')

if st.session_state.texto:
    st.markdown("""
        ##### Eis o que eu penso sobre você ...
    """)