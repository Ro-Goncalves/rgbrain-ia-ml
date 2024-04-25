import streamlit as st
from streamlit_option_menu import option_menu
import os

def app_menu():
    st.header("Laboratórios")
    st.page_link("pages/laboratorio_ocr.py", label="OCR")
    st.divider()
    st.subheader("Experimentos")
    st.session_state.experimento = option_menu(
        menu_title = None,
        options = ["Sobre o Laboratório", "Experimentos", "Cientista"],
        icons=['car-front', 'droplet-half', 'emoji-sunglasses'],        
        default_index=0,
        styles={
            "nav-link": {"color": "black", "--hover-color": "rgba(221, 30, 42, 0.7)"},
            "nav-link-selected": {"background-color": "#DD1E2A", "color": "#ffffff"}
            }   
    )

def laboratorios_menu(nome_laboratorio: str):
    st.header("Ao Inicio")
    st.page_link("streamlit_app.py")
    st.divider()
    st.subheader("Experimentos")
    st.write(nome_laboratorio.split(f"rgbrain_ia_ml{os.sep}pages{os.sep}")[1].split(os.sep))
    #TODO: Buscar de uma configuração