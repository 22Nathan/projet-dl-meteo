import streamlit as st
import pandas as pd
import numpy as np
import geopandas as gpd
import leafmap.kepler as leafmap
# import leafmap
# import streamlit.components.v1 as components
# import leafmap.foliumap as leafmap

# st.balloons()
# st.snow()

geojson = 'geojson/communes-74-haute-savoie.geojson'

m = leafmap.Map(center=[45.9, 6.5], zoom=8)
m.add_geojson(
    geojson, 
    layer_name='MAP', 
    style={ 'fillOpacity': .5 }, 
    fill_colors=["red", "blue"]
)
m.to_streamlit()

st.title('L.A. Beat')