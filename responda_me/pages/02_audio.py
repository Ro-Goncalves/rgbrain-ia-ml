import streamlit as st
import whisper

st.set_page_config(
    page_title = "Audio",
    page_icon = "📈"
)

st.markdown("# Vamos Ouvir e Ser Ouvido")
st.write(
    """This demo illustrates a combination of plotting and animation with
Streamlit. We're generating a bunch of random numbers in a loop for around
5 seconds. Enjoy!"""
)

st.sidebar.header("De-me o seu audio")
audio = st.sidebar.file_uploader("quero ouvi-lo", type=['mp3', 'wav'])

model = whisper.load_model('small')
st.text('Wisper Model Loaded')

if st.sidebar.button('Transcribe Audio'):
    if audio is not None:
        st.sidebar.success('Transcribing Audio')
        transcription = model.transcribe(audio.name)
        st.sidebar.success('Transcription Complete')
        st.markdown(transcription['text'])
    else:
        st.sidebar.error('Please upload an audio file')

st.sidebar.header('Play Original Audio File')
st.sidebar.audio(audio)