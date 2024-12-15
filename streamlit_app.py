import streamlit as st
from transformers import pipeline
import torch

# Select GPU if available, otherwise CPU
device = 0 if torch.cuda.is_available() else -1

# Load the model using pipeline
pipe = pipeline("sentiment-analysis",
                model="azizp128/javanese-sentiment-analysis-indobert")

# Initialize session state for result
if "result" not in st.session_state:
    st.session_state.result = None

st.markdown(
    """
    <h1 style="text-align: center; font-family: sans-serif;">
    Analisis Sentimen Bahasa Jawa Ngoko Lugu
    </h1>
    <hr>
    """,
    unsafe_allow_html=True
)

# Description
st.write("Model analisis sentimen berbasis IndoBERT yang dapat memprediksi sentimen positif atau negatif dari teks berbahasa Jawa Ngoko Lugu.")

# User input
user_input = st.text_input("Input", placeholder="Masukkan teks")

# Examples
options = ["Aku tresno banget karo koe mas.",
           "Mbok ojo dadi wong sing nganyeli.",
           "Teles kebes netes eluh neng dadaku.",
           "Aku sayang karo koe beb, tapi ngapusi",
           "Sedih aku. Lagi mangan iwakku malah dicolong pitek"]
selection = st.segmented_control(
    "Examples", options
)

# Prediction
if selection:
    st.session_state.result = pipe(selection)

if user_input:
    st.session_state.result = pipe(user_input)

# Display results if available
if st.session_state.result:
    for res in st.session_state.result:
        st.write("Prediction")
        st.success(res['label'].capitalize())
        st.write("Score")
        st.success(round(res['score'], 4))
