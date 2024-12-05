import gradio as gr

name = "models/azizp128/javanese-sentiment-analysis-indobert"
title = "Analisis Sentimen Bahasa Jawa Ngoko Lugu"
descriptions = "Model analisis sentimen yang dapat memprediksi sentimen positif atau negatif dari teks berbahasa Jawa Ngoko Lugu."
article = """#### Note: Refresh halaman jika stuck di proses prediksi."""
examples = [["Aku tresno banget karo koe mas."],
            ["Mbok ojo dadi wong sing nganyeli."],
            ["Teles kebes netes eluh neng dadaku."],
            ["Aku sayang karo koe beb, tapi ngapusi"],
            ["Sedih aku. Lagi mangan iwakku malah dicolong pitek"]]

demo = gr.Interface.load(name=name, title=title, description=descriptions,
                         article=article, examples=examples, allow_flagging="auto")

if __name__ == "__main__":
    demo.launch()
