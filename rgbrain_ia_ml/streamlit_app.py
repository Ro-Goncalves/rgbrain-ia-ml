import streamlit as st

from utils.menus import app_menu
from utils import secrets

secrets.carregar_secrets()

st.set_page_config(
    page_title = "RGBRIAN - AI ML",
    page_icon = "🧑‍🔬",
    layout="centered"
)

def states_iniciais():
    if 'experimento' not in st.session_state:
        st.session_state.experimento = None

states_iniciais()

with st.sidebar:    
    app_menu()

if st.session_state.experimento == "Sobre a Instituição":

    st.markdown("<h1 align='center'><b> Bem Vindo à Instituição <br> RGBRIAN - AI ML", unsafe_allow_html=True)
    st.markdown(
        """
        Nosso objetido na **RGBRIAN - AI ML** ***LABS*** é criar laboratórios para testes em *animais virtuais*
        sobre tecnologias voltadas à Inteligência Atificial e Aprendizagem de Máguina.

        Nossas ideias provêm das profundezas do cêrebro, ***BRAIN***, de nosso fundador Rodrigo Gonçalves, ***RG***. *Se prepare-se*
        para ver, ou ler, ou ouvir, ideias psicodelicas provenientes de um fluxo de pensamento sem filtro.

        >Brincadeiras à parte, meu objetivo com esse projeto é compartilhar o que estou pensando e estudando sobre tecnologias
        voltadas à AI e ML
    """)

if st.session_state.experimento == "Laboratórios":
    st.markdown("<h1 align='center'><b> Laboratórios", unsafe_allow_html=True)
    st.markdown("""
        Nossa instituição possui vários **LABS**, cada um com objetivos diferentes. Segue uma breve descrição sobre eles

        ## Laboratório - OCR

        Os ***ratos-imagem*** são, ou eram, um grande desafio para os computadores, esses meio que não conseguiam se cominucar com
        aqueles. Eis que surgem o OCR, dando a capacitade dos computadores verem os **ratos-imagem** e passar um **feedback** ao *humanos* 
        do que foi possível ***"ler"***

        ### Experimento - Contato em Primeiro Grau

        Vulgo **Hello Word** em OCR. 
        
        >**\maquina:** Dado um ***rato-imagem*** me retorne o que você consegue "ler" com as bibliotecas:  
        **EasyOCR**, ...
    """)

if st.session_state.experimento == "Cientista":
    st.markdown("<h1 align='center'><b> Cientista", unsafe_allow_html=True)
    st.markdown("""
        Eis que apresento-vôs nosso **cientista-mor** e **fundador**

        Rodrigo Gonçalves
        
        [![LinkedIn](https://img.icons8.com/?id=13930&format=png)](https://linkedin.com/in/)
        [![GitHub](https://img.icons8.com/?id=AZOZNnY73haj&format=png)](https://github.com/)
    """)