import streamlit as st

from utils.menus import laboratorios_menu
from utils.misc import new_line
from utils.configuracoes_paginas import configura_pagina
from pages.laboratorio_ocr.experimentos_ocr_pages import experimento_ocr_primeiro_contato

st.set_page_config(page_title="LAB OCR", layout="centered")

def state_inicial():
    if 'configuracoes_pagina' not in  st.session_state:
        st.session_state.configuracoes_pagina = None

state_inicial()

st.session_state.configuracoes_pagina = configura_pagina(__file__)
#Colocar as configurações em state, sempre limpar o state ao entrar em um app
#Ver utils.reset_session_state_key de MY-SUPERAPP


with st.sidebar:
    laboratorios_menu(__file__)

if st.session_state.experimento == "Laboratório - OCR":
    st.markdown("# LABORATÓRIO OCR")

    st.markdown("""
        Seja muito bem vindo aos meus experimentos com **OCR**.
        Verá que eu sou meio louco e penso um tanto de coisas extranhas
        e abstratas. Mas espero que o conteúdo encontrado faça mais
        sentido para você do que para mim.
    """)

if st.session_state.experimento == "Contato em Primeiro Grau":
    experimento_ocr_primeiro_contato()

if st.session_state.experimento == "Contato em Segundo Grau":
    "Segundo Grau"

