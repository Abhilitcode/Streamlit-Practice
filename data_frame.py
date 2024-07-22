import streamlit as st 
import pandas as pd 
import numpy as np

excel_file_path = "C:\\Users\\HP\\Downloads\\streamlit practice\\Customer_dataset_OTT_subcription.xlsx"

df = pd.read_excel(excel_file_path)

csv_data = df.to_csv(index=False)

st.dataframe(df)