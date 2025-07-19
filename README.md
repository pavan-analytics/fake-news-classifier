# Fake-News-Classifier-Using-LSTM-and-Bidirectional-LSTM-RNN

A web app to detect fake news articles using deep learning (LSTM and Bidirectional LSTM) powered by TensorFlow and deployed with Streamlit.

---

## 🚀 Live Demo

👉 [Click here to try it online](https://your-app-name.streamlit.app)  
*(Replace with your actual Streamlit Cloud link after deployment)*

---

## 📌 Features

- Accepts any text or news article
- Cleans and preprocesses input text
- Predicts whether the news is **Fake** or **Real**
- Displays confidence score
- Clean and interactive Streamlit web interface

---

## 🧠 Model Details

- Trained using LSTM & BiLSTM on a labeled Fake News dataset
- Tokenization using Keras Tokenizer
- Padded sequences to fixed length (300 words)
- Saved using Keras `.keras` format
- Tokenizer saved as `tokenizer.json`

---

## 🛠 Installation

### ▶️ Run Locally

1. Clone the repository
2. Install dependencies
3. Run the app

```bash
git clone https://github.com/pavan-analytics/fake-news-classifier.git
cd fake-news-classifier
pip install -r requirements.txt
streamlit run fake_news.py

---

☁️ Deploy on Streamlit Cloud
Push this project to a GitHub repo
Go to https://streamlit.io/cloud
Connect your repo and deploy
Set app.py as the entry point
Share your app URL with friends!

---

💬 Test Example (Fake News)

NASA confirms the Earth will experience 15 days of complete darkness in November due to a rare cosmic alignment between Jupiter and Pluto.

Expected Output: 🔴 Fake News

---

🧪 Built With
Python 3
TensorFlow / Keras
Streamlit
NLTK
NumPy

---

📋 requirements.txt
Edit
streamlit
tensorflow
nltk
numpy
