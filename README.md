# Deskripsi
Moodel Deep Learning berbasis IndoBERT yang dapat memprediksi sentimen ‘positif’ atau ‘negatif’ pada teks berbahasa Jawa Ngoko Lugu. Model ini dilatih pada dataset yang diperoleh dari website Twitter/X melalui metode crawling, dan dilakukan proses pelabelan secara manual oleh peneliti. 

Model pre-trained yang digunakan pada penelitian ini adalah [IndoBERT-Base-P1](https://huggingface.co/indobenchmark/indobert-base-p1 ). Sebelum proses pelatihan model, preprocessing dataset dilakukan untuk membersihkan teks dari karakter-karakter yang tidak relevan untuk kasus analisis sentimen. 

Hasil akhir model di-upload ke [Hungging Face Hub](https://huggingface.co/docs/hub/en/index) dan di-deploy ke [Streamlit](https://www.streamlit.io) melalui API [Hungging Face Inference Endpoints](https://huggingface.co/inference-endpoints/dedicated) yang dapat diakses melalui [Analisis Sentimen Bahasa Jawa](https://huggingface.co/azizp128/javanese-sentiment-analysis-indobert).

Penjelasan lebih detail terkait penelitian ini dapat dibaca melalui paper: [Penerapan Metode Transfer Learning Pada Indobert Untuk Analisis Sentimen Teks Bahasa Jawa Ngoko Lugu](https://e-jurnal.stmikbinsa.ac.id/index.php/simkom/article/view/478).

- Playground : [Analisis Sentimen Bahasa Jawa Ngoko Lugu](https://analysis-sentimen-bahasa-jawa-ngoko-lugu.streamlit.app/)
- Model on HunggingFace : [Analisis Sentimen Bahasa Jawa](https://huggingface.co/azizp128/javanese-sentiment-analysis-indobert)
- IndoBERT Pre-trained model : [IndoBERT Base Model P1](https://huggingface.co/indobenchmark/indobert-base-p1)
- Paper : [Penerapan Metode Transfer Learning Pada Indobert Untuk Analisis Sentimen Teks Bahasa Jawa Ngoko Lugu](https://e-jurnal.stmikbinsa.ac.id/index.php/simkom/article/view/478)

# Screenshot
## Streamlit
![Streamlit Web Page Screenshot](https://raw.githubusercontent.com/azizp128/analisis-sentimen-bahasa-jawa-indobert/refs/heads/main/assets/streamlit-screenshot.png)

## Gradio
![Gradio Web Page Screenshot](https://raw.githubusercontent.com/azizp128/analisis-sentimen-bahasa-jawa-indobert/refs/heads/main/assets/gradio-screenshot.png)
