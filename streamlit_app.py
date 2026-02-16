import streamlit as st
import pandas as pd

st.title("⚙️ Machine Learning App")
st.info("This is app builds a machine learning model")

df = pd.read_excel("https://github.com/Mohamedtarek00212/dp-machinelearning/blob/master/penguins_cleaned.xlsx")
df
