import streamlit as st
import pandas as pd

st.title("⚙️ Machine Learning App")
st.info("This is app builds a machine learning model")

# الرابط الخام (Raw) للملف من جيت هاب
url = "https://raw.githubusercontent.com/Mohamedtarek00212/dp-machinelearning/master/penguins_cleaned.xlsx"

# قراءة الملف مباشرة من الرابط
df = pd.read_excel(url)

# عرض الداتا
st.write(df)
