import streamlit as st
import pickle
import os

@st.cache_resource
def load_model():
    # Ambil folder utama proyek (naik 1 tingkat dari /pages)
    base_dir = os.path.dirname(os.path.dirname(__file__))
    model_path = os.path.join(base_dir, "model.pkl")
    
    # Buka model dari folder utama
    with open(model_path, "rb") as f:
        return pickle.load(f)

model = load_model()
