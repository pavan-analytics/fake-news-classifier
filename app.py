<<<<<<< HEAD
import streamlit as st
import re
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import tokenizer_from_json
import json
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# Constants
MAX_LEN = 300

# Load tokenizer
with open("tokenizer.json", "r") as f:
    tokenizer_json=f.read()
    tokenizer = tokenizer_from_json(tokenizer_json)

# Load model
model = load_model("bilstm_fake_news_model.keras")

# Clean text
def clean_text(text):
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    text = text.lower().split()
    words = [word for word in text if word not in stop_words]
    return ' '.join(words)

# Predict
def predict_news(text):
    cleaned = clean_text(text)
    sequence = tokenizer.texts_to_sequences([cleaned])
    padded = pad_sequences(sequence, maxlen=MAX_LEN)
    prediction = model.predict(padded)[0][0]
    label = "🟢 Real News" if prediction > 0.5 else "🔴 Fake News"
    confidence = prediction if prediction > 0.5 else 1 - prediction
    return label, round(confidence * 100, 2)

# Streamlit UI
st.set_page_config(page_title="Fake News Classifier", page_icon="📰")
st.title("📰 Fake News Classifier (BiLSTM)")
st.markdown("Enter a news article to check if it's real or fake.")

user_input = st.text_area("Paste news content:")

if st.button("Classify"):
    if not user_input.strip():
        st.warning("Please enter some text.")
    else:
        label, conf = predict_news(user_input)
        st.success(f"Prediction: {label}")
        st.info(f"Confidence: {conf}%")
=======
import streamlit as st
import re
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.preprocessing.text import tokenizer_from_json
import json
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')
stop_words = set(stopwords.words('english'))

# Constants
MAX_LEN = 300

# Load tokenizer
with open("tokenizer.json", "r") as f:
    tokenizer_json=f.read()
    tokenizer = tokenizer_from_json(tokenizer_json)

# Load model
model = load_model("bilstm_fake_news_model.keras")

# Clean text
def clean_text(text):
    text = re.sub(r'[^a-zA-Z]', ' ', text)
    text = text.lower().split()
    words = [word for word in text if word not in stop_words]
    return ' '.join(words)

# Predict
def predict_news(text):
    cleaned = clean_text(text)
    sequence = tokenizer.texts_to_sequences([cleaned])
    padded = pad_sequences(sequence, maxlen=MAX_LEN)
    prediction = model.predict(padded)[0][0]
    label = "🟢 Real News" if prediction > 0.5 else "🔴 Fake News"
    confidence = prediction if prediction > 0.5 else 1 - prediction
    return label, round(confidence * 100, 2)

# Streamlit UI
st.set_page_config(page_title="Fake News Classifier", page_icon="📰")
st.title("📰 Fake News Classifier (BiLSTM)")
st.markdown("Enter a news article to check if it's real or fake.")

user_input = st.text_area("Paste news content:")

if st.button("Classify"):
    if not user_input.strip():
        st.warning("Please enter some text.")
    else:
        label, conf = predict_news(user_input)
        st.success(f"Prediction: {label}")
        st.info(f"Confidence: {conf}%")
>>>>>>> 8e1de6ec49f3350033bbb23f294a039626c0e2aa
