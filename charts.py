import streamlit as st
import pandas as pd
import numpy as np 
import matplotlib.pyplot as plt

import altair as alt

data = pd.DataFrame(np.random.randn(100,3),columns=['a','b','c'])

st.image("Abhishek_Khale_passport_size_photo.jpg")
#we can also try st.video() or st.audio
city = pd.DataFrame({
    'Location': ['Location1', 'Location2', 'Location3'],
    'LAT': [40.7128, 34.0522, 51.5074],  # Example latitude values
    'LON': [-74.0060, -118.2437, -0.1278]  # Example longitude values
})

st.map(city)

fig, ax = plt.subplots()
plt.scatter(data['a'],data['b']) 
st.pyplot(fig)
st.title("Cluster plot")

chart = alt.Chart(data).mark_point().encode(
    x= 'a',y='b',tooltip=['a','b']
)

#it is used to draw a flow chart
st.graphviz_chart("""
digraph{
watch -> like
like -> share
share -> subscribe
share -> watch              
}
""")
st.altair_chart(chart,use_container_width=True)
st.line_chart(data)

st.bar_chart(data)

st.area_chart(data)


