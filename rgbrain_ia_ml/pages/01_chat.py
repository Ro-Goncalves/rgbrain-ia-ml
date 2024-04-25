import streamlit as st
from utils import chatbot, text
from streamlit_chat import message

def main():
    
    st.set_page_config(
        page_title='Chat',
        page_icon=':books:'
    )
    
    st.header('Vamos Conversar Sobre')
    user_question = st.text_input('Diga-me o que desejas!!!')
    
    if('conversation' not in st.session_state):
        st.session_state.conversation = None
        
    if user_question:        
        try:
            response = st.session_state.conversation(user_question)['chat_history']
        except:
           st.session_state.conversation = chatbot.create_conversation_chain()            
           response = st.session_state.conversation(user_question)['chat_history']
            
        for i, text_message in enumerate(response):                
            if(i % 2 == 0):
                message(text_message.content, is_user=True, key=str((i)) + '_user')
            else:
                message(text_message.content, is_user=False, key=str((i)) + '_bot')
        
        print(st.session_state.conversation.combine_docs_chain)
    
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