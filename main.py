import pandas as pd
import pandas_profiling
import streamlit as st

from streamlit_pandas_profiling import st_profile_report
x=st.file_uploader("Choose a CSV file")
if(x):
  
  df = pd.read_csv(x)
  pr = df.profile_report()

  st_profile_report(pr)
