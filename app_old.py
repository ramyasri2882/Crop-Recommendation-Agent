import streamlit as st
import pandas as pd
import joblib
import os
from datetime import datetime

# Load trained model
model = joblib.load("crop_recommendation_model.pkl")

# Load label encoder
encoder = joblib.load("label_encoder.pkl")
st.title("🌾 Crop Recommendation Agent")

st.write("Enter soil and weather details to get the best crop recommendation.")

n = st.number_input("Nitrogen (N)", min_value=0)

p = st.number_input("Phosphorus (P)", min_value=0)

k = st.number_input("Potassium (K)", min_value=0)

temperature = st.number_input("Temperature (°C)")

humidity = st.number_input("Humidity (%)")

ph = st.number_input("pH Value")

rainfall = st.number_input("Rainfall (mm)")

# Predict Button
if st.button("🌱 Predict Crop"):

    # Prepare input data
    sample = [[
        n,
        p,
        k,
        temperature,
        humidity,
        ph,
        rainfall
    ]]

    # Predict crop
    prediction = model.predict(sample)

    # Convert numeric label to crop name
    crop = encoder.inverse_transform(prediction)

    # Display result
    st.success(f"✅ Recommended Crop: {crop[0]}")