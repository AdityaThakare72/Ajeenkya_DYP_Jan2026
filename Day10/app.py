import streamlit as st
import joblib
import pandas as pd
import numpy as np
st.title("Grape Quality Prediction")
st.write("this is the demo app for grape prediction")

"""
COLOR_INTENSITY = st.number_input("Color Intensity")
FLAVANOIDS = st.number_input("Flavanoids")
PROLINE = st.number_input('Proliine')
TEMPERATURE = st.number_input('Temperature')
FER_P2O5_PER = st.number_input('Fert_p205_per')
# convert this input to dataframe for scaling and prediction
user_input = pd.DataFrame([[COLOR_INTENSITY, FLAVANOIDS, PROLINE, TEMPERATURE, FER_P2O5_PER]],
columns= ['COLOR_INTENSITY', 'FLAVANOIDS', 'PROLINE', 'TEMPERATURE',

'FER_P2O5_PER'])

# load the scaler and model
scaler = joblib.load('scaler.pkl')
model = joblib.load('model.pkl')
scaled_input = scaler.transform(user_input)
prediction = model.predict(scaled_input)
st.write(f"Your Grape Quality Is {prediction[0]}")"""