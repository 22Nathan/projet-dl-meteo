import streamlit as st
import pandas as pd
import numpy as np
import geopandas as gpd
import pickle
import leafmap.kepler as leafmap
import matplotlib.pyplot as plt

with open('models_ARIMA/arima_model_outremer_shrr.pkl', 'rb') as f:
    model_rr = pickle.load(f)

with open('models_ARIMA/arima_model_outremer_shtn.pkl', 'rb') as f:
    model_tn = pickle.load(f)

with open('models_ARIMA/arima_model_outremer_shtx.pkl', 'rb') as f:
    model_tx = pickle.load(f)

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

st.write('Moyenne mensuelle de la température minimale sous abri en °C')
number_tn = st.number_input('TN / ensoleillement |> nb de mois', min_value=0, max_value=100, step=1)
if number_tn:
    predictions_tn = model_tn.forecast(steps=number_tn)

    date_range = pd.date_range(
        start='2024-01-01', 
        periods=len(predictions_tn), 
        freq='M'
    )
    predictions_df = pd.DataFrame({ 'Date': date_range, 'Predicted Value': predictions_tn })
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