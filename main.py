import pandas as pd
import pandas_profiling
import streamlit as st

from streamlit_pandas_profiling import st_profile_report

st.write("Auto Exploratory data analysis (EDA)")
x=st.file_uploader("Upload your CSV or excel file")
if(x):
  
  df = pd.read_csv(x)
  pr = df.profile_report()

  st_profile_report(pr)
