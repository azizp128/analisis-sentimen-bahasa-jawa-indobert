import gradio as gr
import torch
from transformers import pipeline

name = "models/azizp128/javanese-sentiment-analysis-indobert"
title = "Analisis Sentimen Bahasa Jawa Ngoko Lugu"
descriptions = "Model analisis sentimen yang dapat memprediksi sentimen positif atau negatif dari teks berbahasa Jawa Ngoko Lugu."
article = """#### Note: Refresh halaman jika stuck di proses prediksi."""
examples = [["Aku tresno banget karo koe mas."],
            ["Mbok ojo dadi wong sing nganyeli."],
            ["Teles kebes netes eluh neng dadaku."],
            ["Aku sayang karo koe beb, tapi ngapusi"],
            ["Sedih aku. Lagi mangan iwakku malah dicolong pitek"]]

# Select GPU if available, otherwise CPU
device = 0 if torch.cuda.is_available() else -1

# Load the model using pipeline
pipe = pipeline("sentiment-analysis",
                model="azizp128/javanese-sentiment-analysis-indobert", device=device, torch_dtype=torch.float16)


# Define the function for prediction
def predict_sentiment(text):
    result = pipe(text)
    return {res["label"]: res["score"] for res in result}


# Define the Gradio interface
interface = gr.Interface(
    fn=predict_sentiment,
    inputs="text",
    outputs="label",
    title=title, description=descriptions, article=article, examples=examples, flagging_mode="auto"
)

if __name__ == "__main__":
    # Launch the app
    interface.launch()
