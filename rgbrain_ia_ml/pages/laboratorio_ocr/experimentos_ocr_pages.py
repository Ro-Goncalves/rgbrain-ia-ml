
import streamlit as st
from utils.misc import new_line
from servicos.experimentos_ocr_servico import extrai_texto_com_easyocr, extrai_texto_com_pytesseract


def experimento_ocr_primeiro_contato():    
    st.markdown("<h1 align='center'><b> Experimento - Contato em Primeiro Grau", unsafe_allow_html=True)
    st.markdown("""
        Aqui iremos mostrar o inicio dessa tecnologia. Coloque um rato-imagem o transfomaremos em texto 
        utilizando as seguintes bibliotecas:
                
        - **keras_ocr**
        - **pytesseract**
        - **easyocr**
                
    """)
    st.divider()
    st.markdown("<h3 align='center'><b> Experimentos", unsafe_allow_html=True)
    if imagem := st.file_uploader(
        label="Insira a Imagem",
        type=["png", "jpg", "jpeg"],
    ):
        st.markdown("Imagem Carregada")
        st.image(imagem, caption="Imagem")

        col_easyocr, col_kerasocr, col_pytesseract = st.columns(3, gap="small")
        with col_easyocr:
            st.markdown("#### EasyOCR")
            st.write(extrai_texto_com_easyocr(imagem))

        with col_kerasocr:
            st.markdown("#### KerasOCR")
            #st.markdown(extrai_texto_com_keras_ocr(imagem))

        with col_pytesseract:
            st.markdown("#### Pytesseract")
            st.markdown(extrai_texto_com_pytesseract(imagem))
   