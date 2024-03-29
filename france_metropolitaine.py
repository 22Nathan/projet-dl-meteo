import streamlit as st
import pandas as pd
import numpy as np
import geopandas as gpd
import pickle
import leafmap.kepler as leafmap
import matplotlib.pyplot as plt
# import leafmap
# import streamlit.components.v1 as components
# import leafmap.foliumap as leafmap

# geojson = 'geojson/communes-74-haute-savoie.geojson'

# m = leafmap.Map(center=[45.9, 6.5], zoom=8)
# m.add_geojson(
#     geojson, 
#     layer_name='MAP', 
#     style={ 'fillOpacity': .5 }, 
#     fill_colors=["red", "blue"]
# )

# gdf = gpd.read_file(geojson)
# for index, row in gdf.iterrows():
#     region_geojson = row.geometry.__geo_interface__
#     m.add_geojson(region_geojson, layer_name=row['nom'], fill_colors=['red'], style={'fillOpacity': .5})

# m.to_streamlit()

# components.html(m.to_html(read_only=True), width=600, height=600)

with open('models_ARIMA/arima_model_in.pkl', 'rb') as f:
    model_in = pickle.load(f)

with open('models_ARIMA/arima_model_rr.pkl', 'rb') as f:
    model_rr = pickle.load(f)

with open('models_ARIMA/arima_model_tx.pkl', 'rb') as f:
    model_tx = pickle.load(f)

# st.title('L.A. Beat 🦅')

# col1, col2 = st.columns(2)
# with col1:
#     if st.button('neige'):
#         st.snow()
# with col2:
#     if st.button('ballons'):
#         st.balloons()
    
st.title('Projet IA - prédictions météologiques')

st.write('Cumul mensuel des hauteurs de précipitation en mm')
number_rr = st.number_input('RR / précipitation |> nb de mois', min_value=0, max_value=100, step=1)
if number_rr:
    predictions_rr = model_rr.forecast(steps=number_rr)

    date_range = pd.date_range(
        start='2024-01-01', 
        periods=len(predictions_rr), 
        freq='M'
    )
    predictions_df = pd.DataFrame({ 'Date': date_range, 'Predicted Value': predictions_rr })
    predictions_df.set_index('Date', inplace=True)
    st.line_chart(predictions_df)

###

st.write('Cumul mensuel des durées d\'insolation en heures')
number_in = st.number_input('IN / ensoleillement |> nb de mois', min_value=0, max_value=100, step=1)
if number_in:
    predictions_in = model_in.forecast(steps=number_in)

    date_range = pd.date_range(
        start='2024-01-01', 
        periods=len(predictions_in), 
        freq='M'
    )
    predictions_df = pd.DataFrame({ 'Date': date_range, 'Predicted Value': predictions_in })
    predictions_df.set_index('Date', inplace=True)
    st.line_chart(predictions_df)

###

st.write('Moyenne mensuelle de la température maximale sous abri en °C')
number_tx = st.number_input('TX / température |> nb de mois', min_value=0, max_value=100, step=1)
if number_tx:
    predictions_tx = model_tx.forecast(steps=number_tx)

    date_range = pd.date_range(
        start='2024-01-01', 
        periods=len(predictions_tx), 
        freq='M'
    )
    predictions_df = pd.DataFrame({ 'Date': date_range, 'Predicted Value': predictions_tx })
    predictions_df.set_index('Date', inplace=True)
    st.line_chart(predictions_df)