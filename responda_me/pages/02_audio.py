import streamlit as st
import whisper
import torch
import numpy as np
import datetime
import os

from audio_recorder_streamlit import audio_recorder

model = whisper.load_model('small')

def save_audio_file(audio_bytes, file_extension):   
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    file_name = f"audio_{timestamp}.{file_extension}"

    with open(file_name, "wb") as f:
        f.write(audio_bytes)

    return file_name

st.set_page_config(
    page_title = "Audio",
    page_icon = "📈"
)

#tab1, tab2 = st.tabs(["Record Audio", "Upload Audio"])

# # Record Audio tab
# with tab1:
#     audio_bytes = audio_recorder()
#     if audio_bytes:
#         st.audio(audio_bytes, format="audio/wav")
#         save_audio_file(audio_bytes, "mp3")

# # Upload Audio tab
# with tab2:
#     audio_file = st.file_uploader("Upload Audio", type=["mp3", "mp4", "wav", "m4a"])
#     if audio_file:
#         file_extension = audio_file.name.split('.')[1]        
#         save_audio_file(audio_file.read(), file_extension)
   

st.markdown("# Vamos Ouvir e Ser Ouvido")
st.write(
    """Essa demo tenta transcrever um audio em texto. Vamos ver se conseguimos"""
)

st.sidebar.header("De-me o seu audio")
audio = st.sidebar.file_uploader("quero ouvi-lo", type=['mp3', 'wav', 'm4a'])

# device = 'cuda' if torch.cuda.is_available() else 'cpu'


if st.sidebar.button('Transcribe Audio'):
    if audio:
        file_extension = audio.name.split('.')[1]        
        audio_saved = save_audio_file(audio.read(), file_extension)
        transcription = model.transcribe(audio_saved)
       
        st.markdown(transcription['text'])
    else:
        st.sidebar.error('Please upload an audio file')
        
# Save the transcript to a text file
# with open("transcript.txt", "w") as f:
#     f.write(transcription)


st.sidebar.header('Play Original Audio File')
st.sidebar.audio(audio)

# Provide a download button for the transcript
#st.sidebar.download_button("Download Transcript", transcription)