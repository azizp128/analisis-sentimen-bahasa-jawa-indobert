import gradio as gr
from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch

# Load the model and tokenizer
model_name = "models/azizp128/jawa-sentiment-analysis-indobert"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

# Prediction function
def predict(text):
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    with torch.no_grad():
        outputs = model(**inputs)
    logits = outputs.logits
    probabilities = torch.nn.functional.softmax(logits, dim=1)
    predicted_class_id = probabilities.argmax().item()
    labels = {0: "negative", 1: "positive"}
    return labels[predicted_class_id]

# Gradio interface setup
title = "Analisis Sentimen Bahasa Jawa Ngoko Lugu"
description = "Analisis Sentimen Bahasa Jawa adalah aplikasi yang dapat memprediksi sentimen positif atau negatif dari teks kalimat berbahasa Jawa Ngoko Lugu."
article = "#### Note: Refresh halaman jika stuck di proses prediksi."
examples = [
    ["Aku tresno banget karo koe mas."], 
    ["Mbok ojo dadi wong sing nganyeli."], 
    ["Teles kebes netes eluh neng dadaku."],
    ["Aku sayang karo koe beb, tapi ngapusi"],
    ["Sedih aku. Lagi mangan iwakku malah dicolong pitek"]
]

demo = gr.Interface(
    fn=predict,
    inputs="textbox",
    outputs="label",
    title=title,
    description=description,
    article=article,
    examples=examples,
    allow_flagging="auto"
)

if __name__ == "__main__":
    demo.launch()
