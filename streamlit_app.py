import streamlit as st
from transformers import pipeline
import torch

# Select GPU if available, otherwise CPU
device = 0 if torch.cuda.is_available() else -1

# Load the model using pipeline
pipe = pipeline("sentiment-analysis",
                model="azizp128/javanese-sentiment-analysis-indobert")

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
st.write("Model analisis sentimen yang dapat memprediksi sentimen positif atau negatif dari teks berbahasa Jawa Ngoko Lugu.")

# User input
user_input = st.text_input("Input:", placeholder="Masukkan teks")

# Prediction
if user_input:
    result = pipe(user_input)
    for res in result:
        st.write("Prediksi:")
        st.success(res['label'])
        st.write("Skor:")
        st.success(res['score'])
