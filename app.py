import streamlit as st
from utils import chatbot, text
from streamlit_chat import message

def main():
    
    st.set_page_config(
        page_title='Converse comigo',
        page_icon=':books:'
    )
    
    st.header('Converse comigo')
    user_question = st.text_input('Pergunte-Me!!')
    
    if('conversation' not in st.session_state):
        st.session_state.conversation = None
        
    if user_question:
        try:
            response = st.session_state.conversation(user_question)['chat_history']
            
            for i, text_message in enumerate(response):
                
                if(i % 2 == 0):
                    message(text_message.content, is_user=True, key=str((i)) + '_user')
                else:
                    message(text_message.content, is_user=False, key=str((i)) + '_bot')
        except:
           st.session_state.conversation = chatbot.create_conversation_chain() 
           
           response = st.session_state.conversation(user_question)['chat_history']
            
            for i, text_message in enumerate(response):                
                if(i % 2 == 0):
                    message(text_message.content, is_user=True, key=str((i)) + '_user')
                else:
                    message(text_message.content, is_user=False, key=str((i)) + '_bot')
    
    with st.sidebar:
        st.subheader('Seus arquivos')
        
        pdf_docs = st.file_uploader(
            'Carregue os seus arquivos pdf', 
            accept_multiple_files=True)
        
        if st.button('Processar'):
            all_files_text = text.process_files(pdf_docs)
            
            chunks = text.create_text_chunks(all_files_text)
            
            vectorstore = chatbot.create_vectorstore(chunks)
            
            st.session_state.conversation = chatbot.create_conversation_chain(vectorstore)

if __name__ == '__main__':
    main()