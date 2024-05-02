import streamlit as st

from utils.menus import app_menu

st.set_page_config(
    page_title = "Responda Me",
    page_icon = "👋",
    layout="centered"
)

def states_iniciais():
    if 'experimento' not in st.session_state:
        st.session_state.experimento = None

states_iniciais()

st.markdown("# Bem Vinda à Instituição RGBRIAN - IA ML")

st.markdown(
    """
    Responda-Me é uma demo que demonstra às possibilidades que um modelo de LLM tem a oferecer à Br Consorcios.
    
    ## Funcinalidade

    - **Responda-Me Chat**: É um chatbot que responde perguntas baseando-se em um arquivo. Ele se chama Braian e será sempre cortês.
    - **Responda-Me Audio**: É um conversor de audio em texto e texto em audio.
"""
)


with st.sidebar:    
    app_menu()

if st.session_state.experimento:
    st.write(st.session_state.experimento)
