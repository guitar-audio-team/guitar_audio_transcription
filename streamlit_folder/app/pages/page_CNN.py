#IMPORTS
#libraries
import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
#images
cnn = Image.open('/Users/malakoff/code/ybouazza-opthread/guitar_audio_transcription/streamlit_folder/raw_data/cnn_model_img.png')
#MISE EN PAGE
st.markdown("""# How did we build our CNN model?
Our model is a multitask learning keras model for classifiacation.""")

st.image(cnn, caption="Our CNN model")
