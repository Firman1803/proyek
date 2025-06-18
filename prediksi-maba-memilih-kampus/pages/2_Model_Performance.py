import streamlit as st
import pandas as pd
import pickle
from sklearn.metrics import classification_report
from sklearn.model_selection import train_test_split

st.title("📈 Model Performance")

@st.cache_resource
def load_model():
    with open("model.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()

df = pd.read_csv("dataset.csv", sep=",")
X = df[['Akreditasi', 'Uang_Kuliah', 'Fasilitas', 'Pelayanan', 'Lokasi']]
y = df['Pilih_PTN']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

y_pred = model.predict(X_test)
st.text("Classification Report:")
st.text(classification_report(y_test, y_pred))
