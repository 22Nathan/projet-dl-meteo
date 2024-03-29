import streamlit as st
import folium
from streamlit_folium import st_folium

m = folium.Map(location=[45.9, 6.5], zoom_start=9)

highlighted_area = folium.Polygon(
    locations=[
        [37.78, -122.42],
        [37.78, -122.40],
        [37.76, -122.40],
        [37.76, -122.42],
    ],
    color='red',
    fill=True,
    fill_color='red'
).add_to(m)

st_data = st_folium(m, width=725)

st.image('./img_HS/1.png')
st.image('./img_HS/2.png')
st.image('./img_HS/3.png')