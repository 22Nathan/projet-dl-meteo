import streamlit as st
import pandas as pd
import numpy as np

import leafmap.kepler as leafmap

geojson = 'geojson/communes-74-haute-savoie.geojson'

with st.echo():
    m = leafmap.Map(center=[45.9, 6.5], zoom=8)
    m.add_geojson(geojson, layer_name="zzzz")
    m.to_streamlit()

st.title('L.A. Beat')