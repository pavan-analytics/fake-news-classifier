# Fake-News-Classifier-Using-LSTM-and-Bidirectional-LSTM-RNN

A deep learning-powered web application to detect fake news articles using Long Short-Term Memory (LSTM) and Bidirectional LSTM models. The app is built with TensorFlow and deployed using Streamlit, making it easy for anyone to interact with the model via a browser.

---

## 📖 Project Explanation

With the explosion of online content and social media, misinformation and fake news have become major challenges. The goal of this project is to build a text classification model that can distinguish between **real** and **fake news articles** based on their content.

### What it does:
- Takes in a news article (or a snippet)
- Cleans and preprocesses the text (stopwords removal, lowercasing, etc.)
- Converts text to padded sequences using a trained tokenizer
- Uses a deep learning model (LSTM/BiLSTM) to classify the news as **Real** or **Fake**
- Displays a confidence score with a simple and intuitive user interface

This project is particularly helpful for:
- Learning how NLP and RNNs work in real-world applications
- Demonstrating end-to-end ML deployment
- Creating a strong portfolio project for data science and ML interviews

---

## 🚀 Live Demo

👉 [Click here to try it online](https://your-app-name.streamlit.app)  
*(Replace with your actual Streamlit Cloud link after deployment)*

---

## 📌 Features

- Accepts any news text input
- Preprocessing: text cleaning + stopword removal
- Predicts: 🔴 Fake News or 🟢 Real News
- Shows confidence score
- Simple Streamlit UI for interactive use

---

## 🧠 Model Details

- Data Source: Kaggle Fake News Dataset (Real + Fake articles)
- Preprocessing: Regex, stopwords, lowercasing
- Tokenizer: Keras `Tokenizer` with `pad_sequences`
- Sequence length: 300 tokens
- Model: BiLSTM (can switch to LSTM)
- Output: Binary classification (Fake or Real)
- Model Format: `.keras`
- Tokenizer saved as: `tokenizer.json`

---


## 🛠 Installation

### ▶️ Run Locally

```bash
git clone https://github.com/pavan-analytics/fake-news-classifier.git
cd fake-news-classifier
pip install -r requirements.txt
streamlit run fake_news.py
````

### ☁️ Deploy on Streamlit Cloud

1. Push this project to a GitHub repo
2. Go to [https://streamlit.io/cloud](https://streamlit.io/cloud)
3. Connect your repo
4. Set `app.py` as the entry point
5. Share your custom link!

---

## 💬 Test Example (Fake News)

```
NASA confirms the Earth will experience 15 days of complete darkness in November due to a rare cosmic alignment between Jupiter and Pluto.
```

Expected Output: 🔴 Fake News

---

## 🧪 Built With

* Python 3
* TensorFlow / Keras
* Streamlit
* NLTK
* NumPy

---

## 📋 requirements.txt

```txt
streamlit
tensorflow
nltk
numpy
```

---

## 📜 License

This project is licensed under the MIT License.

---

## 🙌 Acknowledgments

* [Kaggle Fake News Dataset](https://www.kaggle.com/datasets/clmentbisaillon/fake-and-real-news-dataset)
* Streamlit Team
* TensorFlow/Keras Developers
