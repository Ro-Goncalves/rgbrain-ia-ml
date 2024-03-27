import streamlit as st

st.set_page_config(
    page_title = "Responda Me",
    page_icon = "👋"
)

st.write("# Bem Vinda à Demo RESPONDA-ME! 👋")

st.markdown(
    """
    Responda-Me é uma demo que demonstra às possibilidades que um modelo de LLM tem a oferecer à Br Consorcios.
    
    ## Funcinalidade

    - **Responda-Me Chat**: É um chatbot que responde perguntas baseando-se em um arquivo. Ele se chama Braian e será sempre cortês.
    - **Responda-Me Audio**: É um conversor de audio em texto e texto em audio.
"""
)