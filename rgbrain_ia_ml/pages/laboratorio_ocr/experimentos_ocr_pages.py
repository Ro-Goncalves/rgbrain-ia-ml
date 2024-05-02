
import streamlit as st
from utils.misc import new_line


def experimento_ocr_primeiro_contato():        
    configuracoes_pagina = st.session_state.configuracoes_pagina
    
    st.markdown("<h2 align='center'><b> Configurações", unsafe_allow_html=True)
    new_line(2)

    col_modelo_ocr, col_modelo_llm, col_modelo_prompt = st.columns(3, gap="medium")

    with col_modelo_ocr:
        st.markdown("<h5 align='center'><b> Configurações OCR", unsafe_allow_html=True)
        opcoes_modelo_ocr = []
        for modelos_ocr  in configuracoes_pagina["modelos_ocr"]:
            opcoes_modelo_ocr.append(modelos_ocr["nome"])
        
        opcao_ocr = st.selectbox(
            label="Escolha o OCR",
            options=opcoes_modelo_ocr,
            key="opcao_ocr",
        )

    with col_modelo_llm:
        st.markdown("<h5 align='center'><b> Configurações LLM", unsafe_allow_html=True)
        opcoes_modelo_llm = []
        for modelos_llm  in configuracoes_pagina["modelos_llm"]:
            opcoes_modelo_llm.append(modelos_llm["nome"])
        
        opcao_llm = st.selectbox(
            label="Escolha a LLM",
            options=opcoes_modelo_llm,
            key="opcao_llm",
        )

    with col_modelo_prompt:
        st.markdown("<h5 align='center'><b> Configurações PROMPT", unsafe_allow_html=True)
        opcoes_modelo_prompt = []
        for modelos_prompt  in configuracoes_pagina["modelos_prompt"]:
            opcoes_modelo_prompt.append(modelos_prompt["nome"])
        
        opcao_prompt = st.selectbox(
            label="Escolha o Prompt",
            options=opcoes_modelo_prompt,
            key="opcao_prompt",
        )

    new_line(5)
    st.markdown("<h2 align='center'><b> Experimento", unsafe_allow_html=True)
    new_line(2)

    col_imagem, col_prompt = st.columns(2, gap="medium")

    with col_imagem:
        st.markdown("<h5 align='center'> Carregar Imagem <b>", unsafe_allow_html=True)
        if imagem := st.file_uploader(
            label="Insira a Imagem",
            type=["png", "jpg", "jpeg"],
        ):
            st.image(imagem, caption="Imagem")
            #st.write(extrai_texto_com_easyocr(imagem))

    with col_prompt:
        st.markdown("<h5 align='center'> Conversar Com a Imagem <b>", unsafe_allow_html=True)
        new_line(2)
        
        if prompt := st.chat_input(
            placeholder=f"Conversando com {opcao_llm}",
        ):
            st.chat_message("human").write(prompt)
            st.chat_message("ai").write(f"Olá Sou IA {prompt}")
