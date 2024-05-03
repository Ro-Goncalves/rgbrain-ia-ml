import streamlit as st
from streamlit_option_menu import option_menu
from utils.misc import nome_laboratorio, carregar_configuracoes_pagina
import os

def app_menu():
    st.header("Laboratórios")
    st.page_link("pages/laboratorio_ocr.py", label="OCR", icon="👓")
    st.divider()
    st.subheader("Experimentos")
    st.session_state.experimento = option_menu(
        menu_title = None,
        options = ["Sobre a Instituição", "Laboratórios", "Cientista"],
        icons=['bi-buildings', 'bi-radioactive', 'bi-robot'],        
        default_index=0,
        styles={
            "nav-link": {"color": "black", "--hover-color": "rgba(221, 30, 42, 0.7)"},
            "nav-link-selected": {"background-color": "#DD1E2A", "color": "#ffffff"}
            }   
    )

def laboratorios_menu(arquivo_laboratorio: str):
    laboratorio = nome_laboratorio(arquivo_laboratorio)
    configuracoes_pagina = carregar_configuracoes_pagina()
    st.header("À Instituição")
    st.page_link("streamlit_app.py", label="Instituição", icon="🏰")
    st.divider()
    st.subheader("Experimentos")

    experimentos_opcoes = []
    experimentos_icones = []
    for experimento in configuracoes_pagina[laboratorio]["experimentos"]:
        experimentos_opcoes.append(experimento["nome"])
        experimentos_icones.append(experimento["icone"])

    st.session_state.experimento = option_menu(
        menu_title = None,
        options = experimentos_opcoes,
        icons=experimentos_icones,        
        default_index=0,
        styles={
            "nav-link": {"color": "black", "--hover-color": "rgba(221, 30, 42, 0.7)"},
            "nav-link-selected": {"background-color": "#DD1E2A", "color": "#ffffff"}
            }   
    )