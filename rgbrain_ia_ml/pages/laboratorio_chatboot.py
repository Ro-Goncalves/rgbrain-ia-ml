import streamlit as st
from utils.menus import laboratorios_menu
from pages.laboratorio_ocr.experimentos_chatboot_pages import experimento_ocr_primeiro_contato

st.set_page_config(page_title="LAB CHAT", layout="centered")

def state_inicial():
    if('conversation' not in st.session_state):
        st.session_state.conversation = None

    if 'configuracoes_pagina' not in  st.session_state:
        st.session_state.configuracoes_pagina = None

state_inicial()

with st.sidebar:
    laboratorios_menu(__file__)

if st.session_state.experimento == "Laboratório - CHATBOOT":
    st.markdown("<h1 align='center'><b> Laboratório CHATBOOT", unsafe_allow_html=True)

    st.markdown("""
        Seja muito bem vindo ao meus experimentos com **CHATBOOT**.
        Como não quero perder o bonde, irei começar com bots baseados em ***LLMs***,
        e como sou um asaláriado médio, irei usar modelos abertos disponibilizados
        pela Hugginface.
                
        > Pegue o seu chá e venha comigo nessa viagem.
    """)

if st.session_state.experimento == "Contato em Primeiro Grau":
    experimento_ocr_primeiro_contato()