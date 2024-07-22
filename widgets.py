import streamlit as st 
import matplotlib.pyplot as plt 
import numpy as np
import pandas as pd

st.title("Widgets")
if st.button('click here'):
    st.write('Welcome')

name = st.text_input('Name')
st.write(name)

addresses = st.text_area("Enter your add here")
st.write(addresses)

st.date_input("Enter the date")

st.time_input("Enter the current time")

if st.checkbox("Read the T&C", value=True):
    st.write("Thank you")

rd = st.radio("Columns",['r','g','b'], index =1)
select = st.selectbox("Columns",['r','g','b'],index = 0)

st.write(rd,select)

v3 = st.multiselect("Columns",['r','g','b'])
st.write(v3)

st.slider("Slide it",min_value=10,max_value=100,value=30,step=2)
st.number_input("Numbers",min_value=20,max_value=100,value=30,step=2)

img = st.file_uploader("Upload the image",type=["jpg", "jpeg", "png"])
st.image(img)