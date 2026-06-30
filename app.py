import streamlit as st
import pandas as pd
import joblib
import os
from datetime import datetime

# -------------------------------------------------
# Page Configuration
# -------------------------------------------------
st.set_page_config(
    page_title="Crop Recommendation Agent",
    page_icon="🌾",
    layout="wide"
)

# -------------------------------------------------
# Load Model
# -------------------------------------------------
model = joblib.load("crop_recommendation_model.pkl")
encoder = joblib.load("label_encoder.pkl")

# -------------------------------------------------
# Sidebar
# -------------------------------------------------
st.sidebar.title("🌱 AI Farming Assistant")

st.sidebar.markdown("## Project Features")

st.sidebar.success("✅ Crop Recommendation")
st.sidebar.success("✅ Cultivation Records")
st.sidebar.success("✅ Prediction History")

st.sidebar.markdown("---")

st.sidebar.info("""
### Developed Using

• Python

• Streamlit

• Machine Learning

• Random Forest
""")

# -------------------------------------------------
# Title
# -------------------------------------------------
st.markdown(
"""
<h1 style='text-align:center;color:green;'>
🌾 Crop Recommendation Agent
</h1>
""",
unsafe_allow_html=True
)

st.markdown(
"<h4 style='text-align:center;'>AI Powered Smart Farming Assistant</h4>",
unsafe_allow_html=True
)

st.markdown("---")

# -------------------------------------------------
# Input Section
# -------------------------------------------------

col1, col2 = st.columns(2)

with col1:

    n = st.number_input("Nitrogen (N)", min_value=0)

    p = st.number_input("Phosphorus (P)", min_value=0)

    k = st.number_input("Potassium (K)", min_value=0)

    temperature = st.number_input("Temperature (°C)", format="%.2f")

with col2:

    humidity = st.number_input("Humidity (%)", format="%.2f")

    ph = st.number_input("pH Value", format="%.2f")

    rainfall = st.number_input("Rainfall (mm)", format="%.2f")

# -------------------------------------------------
# Predict Button
# -------------------------------------------------

if st.button("🌱 Predict Crop"):

    sample = [[
        n,
        p,
        k,
        temperature,
        humidity,
        ph,
        rainfall
    ]]

    prediction = model.predict(sample)

    crop = encoder.inverse_transform(prediction)

    st.success(f"✅ Recommended Crop : {crop[0]}")

    st.markdown("---")

    colA, colB = st.columns(2)

    with colA:
        st.metric("🌾 Recommended Crop", crop[0])

    with colB:
        st.metric(
            "📅 Prediction Date",
            datetime.now().strftime("%d-%m-%Y")
        )

    # Save Record

    record = pd.DataFrame({

        "Date & Time":[datetime.now().strftime("%d-%m-%Y %H:%M:%S")],

        "Nitrogen":[n],

        "Phosphorus":[p],

        "Potassium":[k],

        "Temperature":[temperature],

        "Humidity":[humidity],

        "pH":[ph],

        "Rainfall":[rainfall],

        "Recommended Crop":[crop[0]]

    })

    file_name="cultivation_records.csv"

    if os.path.exists(file_name):

        record.to_csv(
            file_name,
            mode="a",
            header=False,
            index=False
        )

    else:

        record.to_csv(
            file_name,
            index=False
        )

# -------------------------------------------------
# Display Records
# -------------------------------------------------

st.markdown("---")

st.subheader("📋 Cultivation Records")

file_name="cultivation_records.csv"

if os.path.exists(file_name):

    history=pd.read_csv(file_name)

    st.metric("📊 Total Predictions",len(history))

    st.dataframe(history,use_container_width=True)

    st.subheader("📊 Crop Prediction Summary")

    crop_counts=history["Recommended Crop"].value_counts()

    st.bar_chart(crop_counts)

    with open(file_name,"rb") as file:

        st.download_button(

            label="⬇️ Download Cultivation Records",

            data=file,

            file_name="cultivation_records.csv",

            mime="text/csv"

        )

    if st.button("🗑️ Clear All Records"):

        os.remove(file_name)

        st.success("Records Deleted Successfully!")

        st.rerun()

else:

    st.info("No cultivation records found.")

# -------------------------------------------------
# Footer
# -------------------------------------------------

st.markdown("---")

st.markdown(
"""
<center>

Developed using ❤️ with Python, Streamlit & Machine Learning

</center>
""",
unsafe_allow_html=True
)