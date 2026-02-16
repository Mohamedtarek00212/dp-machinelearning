import streamlit as st
import pandas as pd

st.title("⚙️ Machine Learning App")
st.info("This is app builds a machine learning model")

with st.expander("Data"):
  url = "https://raw.githubusercontent.com/Mohamedtarek00212/dp-machinelearning/master/penguins_cleaned.xlsx"
  st.write('**Raw data**')
  df = pd.read_excel(url)
  df
