import streamlit as st
import pandas as pd

st.title("📊 Dashboard Data")

df = pd.read_csv("dataset.csv", sep=",")
st.write("### Contoh Data")
st.dataframe(df.head())

st.write("### Statistik Deskriptif")
st.write(df.describe())
