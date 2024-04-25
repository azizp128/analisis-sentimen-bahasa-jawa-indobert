import gradio as gr

name = "models/azizp128/jawa-sentiment-analysis-indobert"
title = "Analisis Sentimen Bahasa Jawa"
descriptions = "Analisis Sentimen Bahasa Jawa adalah aplikasi yang dapat memprediksi sentimen positif atau negatif dari kalimat berbahasa Jawa Ngoko Lugu."
article = """#### Note: Refresh halaman jika stuck di proses prediksi."""
examples = [["Aku tresno banget karo koe mas."], 
    ["Mbok ojo dadi wong sing nganyeli."], 
    ["Teles kebes netes eluh neng dadaku."]]

demo = gr.Interface.load(name=name, title=title, description=descriptions, article=article, examples=examples, allow_flagging="auto")

if __name__ == "__main__":
    demo.launch()
