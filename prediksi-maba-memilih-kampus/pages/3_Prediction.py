import streamlit as st
import pickle
import numpy as np

st.title("🔮 Prediksi Mahasiswa Memilih Kampus")

@st.cache_resource
def load_model():
    with open("model.pkl", "rb") as f:
        return pickle.load(f)

model = load_model()

akreditasi = st.slider("Akreditasi (1-5)", 1, 5, 3)
uang_kuliah = st.slider("Uang Kuliah (1-5)", 1, 5, 3)
fasilitas = st.slider("Fasilitas (1-5)", 1, 5, 3)
pelayanan = st.slider("Pelayanan (1-5)", 1, 5, 3)
lokasi = st.slider("Lokasi (1-5)", 1, 5, 3)

if st.button("Prediksi"):
    features = np.array([[akreditasi, uang_kuliah, fasilitas, pelayanan, lokasi]])
    prediction = model.predict(features)[0]
    if prediction == 1:
        st.success("✅ Mahasiswa kemungkinan memilih kampus ini.")
    else:
        st.error("❌ Mahasiswa kemungkinan **tidak memilih** kampus ini.")
