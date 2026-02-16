import streamlit as st
import pandas as pd

st.title("⚙️ Machine Learning App")
st.info("This is app builds a machine learning model")

with st.expander("Data"):
  url = "https://raw.githubusercontent.com/Mohamedtarek00212/dp-machinelearning/master/penguins_cleaned.xlsx"
  st.write('**Raw data**')
  df = pd.read_excel(url)
  df

  st.write('**X**')
  X = df.drop('species', axis= 1)
  X

  st.write('**y**')
  y = df.species
  y

 with st.expander('Data visualization'):
   # bill_length_mm	bill_depth_mm	flipper_length_mm	body_mass_g
   st.scatter_chart(data= df, x = 
