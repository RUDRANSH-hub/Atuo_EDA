import pandas as pd
from dataprep.eda import create_report
import streamlit as st

# def displayPDF(file):
#     # Opening file from file path
#     with open(file, "rb") as f:
#         base64_pdf = base64.b64encode(f.read()).decode('utf-8')

#     # Embedding PDF in HTML
#     pdf_display = F'<embed src="data:application/pdf;base64,{base64_pdf}" width="700" height="1000" type="application/pdf">'

#     # Displaying File
#     st.markdown(pdf_display, unsafe_allow_html=True)



# st.write("Upload your CSV File")
spectra = st.file_uploader("upload file", type={"csv", "txt"})
if spectra is not None:
    spectra_df = pd.read_csv(spectra)
    # st.write(spectra_df)
    
    
    for i in range(5):

        st.balloons()    
    report = create_report(spectra_df, title='My Report')
    report.show_browser()
