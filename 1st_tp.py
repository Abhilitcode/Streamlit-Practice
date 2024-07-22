import streamlit as st
import pandas as pd
import numpy as np
st.title("Hello World")
st.header("This is a header")
st.subheader("This is a subheader")

st.text("This is a preformatted text cannot change the font here")

st.markdown(""" 
# this is a h1 tag
## this is h2 tag
### this is a h3 tag
:moon:<br>
:sunglasses: 
**bold**          
_italics_
""",True)

st.latex(r'''x^n + y^n = z^n''')
st.write("# Abhishek Khale")
d = {
    'Boy': "Abhishek",
    'Age': 21
}
st.write(d)
st.write(st)

df = pd.read_csv("C:\\Users\\HP\\Downloads\\streamlit practice\\continent.csv")
st.dataframe(df)