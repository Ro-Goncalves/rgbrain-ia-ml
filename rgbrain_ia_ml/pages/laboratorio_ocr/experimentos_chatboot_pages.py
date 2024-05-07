import streamlit as st
from utils import chatbot, text
from streamlit_chat import message
from utils.misc import new_line

def experimento_ocr_primeiro_contato():
    
    st.markdown("<h1 align='center'><b> Experimento - Chatboot com RAG", unsafe_allow_html=True)
    st.markdown("""
        Quase todo mundo deve começar por aqui. A ideia é simples. Dados um arquivo que deverá ser
        utilizado como base de conhecimento, reponda as perguntas do usuário.
                
        **Esse é um resumo simples e direto**
    """)
    new_line(3)

    st.markdown("<h2 align='center'><b> Criando base de Conhecimento", unsafe_allow_html=True)

    if arquivo_pdf := st.file_uploader("Carregar Arquivo Base de Conhecimento", accept_multiple_files=True):
        _, _, col_botao = st.columns(3)
        with col_botao:
            if st.button('Criar Base Conhecimento', use_container_width=True):
                all_files_text = text.process_files(arquivo_pdf)        
                chunks = text.create_text_chunks(all_files_text)
                vectorstore = chatbot.create_vectorstore(chunks)        
                st.session_state.conversation = chatbot.create_conversation_chain(vectorstore)
            
    st.divider()
    if st.session_state.conversation:
        st.markdown("<h2 align='center'><b> Vamos Conversar", unsafe_allow_html=True)

        user_question = st.text_input('Me faça uma pergunta!!!')   
            
        if user_question:
            response = st.session_state.conversation(user_question)['chat_history']
                
            for i, text_message in enumerate(response):                
                if(i % 2 == 0):
                    message(text_message.content, is_user=True, key=str((i)) + '_user')
                else:
                    message(text_message.content, is_user=False, key=str((i)) + '_bot')
            
            print(st.session_state.conversation.combine_docs_chain)