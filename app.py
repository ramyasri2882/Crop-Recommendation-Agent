import streamlit as st
import pandas as pd
import joblib
import os
from datetime import datetime

# ---------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------

st.set_page_config(
    page_title="AI Smart Farming Assistant",
    page_icon="🌾",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ---------------------------------------
# LOAD MACHINE LEARNING MODEL
# ---------------------------------------

model = joblib.load("crop_recommendation_model.pkl")
encoder = joblib.load("label_encoder.pkl")

# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------

st.sidebar.title("🌾 AI Farming Assistant")

st.sidebar.markdown("### Smart Farming using Machine Learning")

st.sidebar.divider()





menu = st.sidebar.radio(

    "📂 Navigation",

    [

        "🏠 Dashboard",

        "🌱 Crop Recommendation",

        "📊 Analytics",

        "🌿 Fertilizer Guide",

        "💰 Profit Estimator",

        "📄 PDF Report",

        "ℹ About"

    ]

)

st.sidebar.divider()

# ---------------------------------------
# LANGUAGE SELECTOR
# ---------------------------------------

language = st.sidebar.selectbox(
    "🌐 Select Language",
    ["English", "తెలుగు", "हिन्दी"],
    key="language_selector"
)

# ---------------------------------------
# TRANSLATION DICTIONARY
# ---------------------------------------

if language == "English":

    text = {
        "dashboard":"🏠 Dashboard",
        "crop":"🌱 Crop Recommendation",
        "analytics":"📊 Analytics",
        "fertilizer":"🌿 Fertilizer Guide",
        "profit":"💰 Profit Estimator",
        "report":"📄 PDF Report",
        "about":"ℹ About",
        "predict":"🌾 Predict Crop",
        "soil":"🌱 Soil & Weather Information",
        "recommended":"Recommended Crop",
        "welcome":"Welcome to the AI Smart Farming Assistant"
    }

elif language == "తెలుగు":

    text = {
        "dashboard":"🏠 డాష్‌బోర్డ్",
        "crop":"🌱 పంట సూచన",
        "analytics":"📊 విశ్లేషణ",
        "fertilizer":"🌿 ఎరువుల సూచన",
        "profit":"💰 లాభాల అంచనా",
        "report":"📄 నివేదిక",
        "about":"ℹ గురించి",
        "predict":"🌾 పంటను సూచించు",
        "soil":"🌱 నేల మరియు వాతావరణ సమాచారం",
        "recommended":"సూచించిన పంట",
        "welcome":"AI స్మార్ట్ వ్యవసాయ సహాయకానికి స్వాగతం"
    }

else:

    text = {
        "dashboard":"🏠 डैशबोर्ड",
        "crop":"🌱 फसल अनुशंसा",
        "analytics":"📊 विश्लेषण",
        "fertilizer":"🌿 उर्वरक मार्गदर्शिका",
        "profit":"💰 लाभ अनुमान",
        "report":"📄 रिपोर्ट",
        "about":"ℹ परिचय",
        "predict":"🌾 फसल बताएं",
        "soil":"🌱 मिट्टी और मौसम की जानकारी",
        "recommended":"अनुशंसित फसल",
        "welcome":"AI स्मार्ट खेती सहायक में आपका स्वागत है"
    }

st.sidebar.success("🤖 Model\n\nRandom Forest")

st.sidebar.info("🎯 Accuracy\n\n99.32%")

st.sidebar.warning("📁 Dataset\n\n2200 Samples")

st.sidebar.divider()

st.sidebar.caption("Developed Using")

st.sidebar.caption("✔ Python")

st.sidebar.caption("✔ Streamlit")

st.sidebar.caption("✔ Machine Learning")

st.sidebar.caption("✔ Random Forest")

st.markdown("""
<h1 style='text-align:center;
color:#22c55e;
font-size:52px;
font-weight:bold;'>

🌾 AI Smart Farming Assistant

</h1>
""", unsafe_allow_html=True)

st.markdown("""
<h4 style='text-align:center;
color:#d1d5db;'>

AI Powered Crop Recommendation using Machine Learning

</h4>
""", unsafe_allow_html=True)

st.markdown("---")

# ---------------------------------------------
# DASHBOARD PAGE
# ---------------------------------------------

if menu == "🏠 Dashboard":

    st.markdown(f"## {text['dashboard']}")

    st.success(text["welcome"])

    c1, c2, c3, c4 = st.columns(4)

    with c1:
        st.metric("🎯 Accuracy", "99.32%")

    with c2:
        st.metric("🤖 Model", "Random Forest")

    with c3:
        st.metric("📁 Dataset", "2200")

    with c4:
        st.metric("🌾 Predictions", "0")

    st.markdown("---")

    st.subheader("📖 About This Project")

    st.write("""
This AI Smart Farming Assistant recommends the best crop
based on soil nutrients and weather conditions using a
Machine Learning Random Forest model.

The application helps farmers make better decisions,
increase productivity and improve crop planning.
""")
    # ---------------------------------------------------
# CROP RECOMMENDATION
# ---------------------------------------------------

if menu == "🌱 Crop Recommendation":

    st.header(text["crop"])

    st.write(text["soil"])
    left, right = st.columns(2)

    with left:

        nitrogen = st.number_input("Nitrogen (N)", value=90)

        phosphorus = st.number_input("Phosphorus (P)", value=42)

        potassium = st.number_input("Potassium (K)", value=43)

        temperature = st.number_input("Temperature (°C)", value=20.8)

    with right:

        humidity = st.number_input("Humidity (%)", value=82.0)

        ph = st.number_input("Soil pH", value=6.5)

        rainfall = st.number_input("Rainfall (mm)", value=202.9)

    predict = st.button(text["predict"])

    if predict:

        sample = [[
            nitrogen,
            phosphorus,
            potassium,
            temperature,
            humidity,
            ph,
            rainfall
        ]]

        prediction = model.predict(sample)

        crop = encoder.inverse_transform(prediction)[0]

        st.success(f"✅ {text['recommended']}: **{crop.upper()}**")

        record = pd.DataFrame({

            "Date":[datetime.now().strftime("%d-%m-%Y %H:%M")],

            "Nitrogen":[nitrogen],

            "Phosphorus":[phosphorus],

            "Potassium":[potassium],

            "Temperature":[temperature],

            "Humidity":[humidity],

            "pH":[ph],

            "Rainfall":[rainfall],

            "Recommended Crop":[crop]

        })

        file_name = "cultivation_records.csv"

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



        

        # ---------------------------------------------------
# ANALYTICS
# ---------------------------------------------------

# ---------------------------------------------------
# ANALYTICS
# ---------------------------------------------------

if menu == "📊 Analytics":

    st.header("📊 Analytics")

    if os.path.exists("cultivation_records.csv"):

        history = pd.read_csv("cultivation_records.csv")

        st.success(f"📊 Total Predictions : {len(history)}")

        st.subheader("📋 Prediction History")

        st.dataframe(history, use_container_width=True)

        st.markdown("---")

        crop_counts = history["Recommended Crop"].value_counts()

        st.subheader("📊 Crop Frequency")

        st.bar_chart(crop_counts)

        st.markdown("---")

        st.subheader("📈 Crop Distribution")

        st.line_chart(crop_counts)

    else:

        st.warning("No prediction history available.")

        # ---------------------------------------------------
# FERTILIZER GUIDE
# ---------------------------------------------------

if menu == "🌿 Fertilizer Guide":

    st.header("🌿 Fertilizer Guide")

    crop = st.selectbox(

        "Select Crop",

        [

            "Rice",
            "Maize",
            "Cotton",
            "Mango",
            "Apple",
            "Banana"

        ]

    )

    fertilizer = {

        "Rice":"Urea + DAP",

        "Maize":"NPK 20:20:20",

        "Cotton":"Potash + Urea",

        "Mango":"Organic Compost",

        "Apple":"Vermicompost",

        "Banana":"NPK 10:26:26"

    }

    st.success(f"Recommended Fertilizer: {fertilizer[crop]}")

    # ---------------------------------------------------
# PROFIT ESTIMATOR
# ---------------------------------------------------

if menu == "💰 Profit Estimator":

    st.header("💰 Profit Estimator")

    st.write("Estimate your expected crop income.")

    crop = st.selectbox(
        "Select Crop",
        [
            "Rice",
            "Maize",
            "Cotton",
            "Banana",
            "Apple",
            "Mango"
        ]
    )

    area = st.number_input(
        "Land Area (Acres)",
        min_value=1.0,
        value=1.0
    )

    yield_per_acre = st.number_input(
        "Expected Yield per Acre (kg)",
        min_value=100,
        value=3000
    )

    market_price = st.number_input(
        "Market Price (₹ per kg)",
        min_value=1,
        value=20
    )

    if st.button("💵 Calculate Income"):

        total_yield = area * yield_per_acre

        income = total_yield * market_price

        st.success(f"🌾 Total Yield : {total_yield:,.0f} kg")

        st.success(f"💰 Estimated Income : ₹ {income:,.0f}")

        # ---------------------------------------------------
# PDF REPORT
# ---------------------------------------------------

if menu == "📄 PDF Report":

    st.header("📄 Reports")

    st.write("Download your cultivation records.")

    file_name = "cultivation_records.csv"

    if os.path.exists(file_name):

        with open(file_name, "rb") as file:

            st.download_button(
                label="⬇ Download Cultivation Records",
                data=file,
                file_name="cultivation_records.csv",
                mime="text/csv"
            )

    else:

        st.warning("No cultivation records found.")

        # ---------------------------------------------------
# ABOUT
# ---------------------------------------------------

if menu == "ℹ About":

    st.header("ℹ About This Project")

    st.markdown("""
### 🌾 AI Smart Farming Assistant

This application recommends the most suitable crop using
Machine Learning based on soil nutrients and weather conditions.

### Technologies Used

- Python
- Streamlit
- Scikit-learn
- Pandas
- Machine Learning
- Random Forest Classifier

### Dataset

Crop Recommendation Dataset

### Developer

**Ramya Sri Jaggarapu**

B.Tech Student

AI & Machine Learning Enthusiast
""")