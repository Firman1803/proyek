import streamlit as st
import pandas as pd

st.title("📊 Dashboard Data")

import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
df = pd.read_csv(os.path.join(BASE_DIR, "dataset.csv"), sep=",")

st.write("### Contoh Data")
st.dataframe(df.head())

st.write("### Statistik Deskriptif")
st.write(df.describe())
