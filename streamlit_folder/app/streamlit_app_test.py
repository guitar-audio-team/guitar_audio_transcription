#IMPORTS
#libraries
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
#images
wav_to_ = Image.open('/Users/malakoff/code/ybouazza-opthread/guitar_audio_transcription/streamlit_folder/raw_data/wav_to_.png')
partition = Image.open('/Users/malakoff/code/ybouazza-opthread/guitar_audio_transcription/streamlit_folder/raw_data/partition.gif')
surprise = Image.open('/Users/malakoff/code/ybouazza-opthread/guitar_audio_transcription/streamlit_folder/raw_data/surprise.png').resize((900, 500))


#audios
audio_file_ex = open('/Users/malakoff/code/ybouazza-opthread/guitar_audio_transcription/streamlit_folder/raw_data/00_BN1-129-Eb_comp_mix.wav', 'rb')
audio_ex = audio_file_ex.read()




#MISE EN PAGE
st.markdown("""# Guitar Audio Transcription
## Batch 1004
Marc-Antoine LE MENTEC, Ethan ROUMI VILLAVERDE, Younès BOUAZZAOUI, Malak BENSALAH""")

st.markdown("""## Our goal:
The aim of our project is to transcribe the audio of a guitar into a partion.
## But what does it actually mean?
We want to go from a .wav audio file to a beautiful partion.""")





st.image(wav_to_, use_column_width=True)




if st.checkbox("Let's go!"):

    st.image(partition, use_column_width=True)

    st.audio(audio_ex, format='audio/ogg')

else:
    st.image(surprise)
