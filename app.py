
import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
from src.predict import load_model, make_prediction
from src.features import preprocess_data
# --------------------------------
# Page Config
# --------------------------------
st.set_page_config(
    page_title="Lagos Rent Intelligence System",
    page_icon="🏠",
    layout="centered"
)

# --------------------------------
# Load Model
# --------------------------------
@st.cache_resource
def load():
    return load_model()


model, columns = load()

df = pd.read_csv("data/lagos_rent.csv")

# Preprocess dataset
df = preprocess_data(df)

# --------------------------------
# Header
# --------------------------------
st.title("🏠 Lagos Rent Intelligence System")

st.info("🚀 AI-powered Lagos Property Rent Prediction")

st.markdown(
    """
Predict estimated Lagos rental prices using Machine Learning.

This system analyzes:
- Location
- Bedrooms
- Property type
- Luxury features
- Furnishing
- Servicing
"""
)

st.markdown("---")

# --------------------------------
# Sidebar
# --------------------------------
st.sidebar.header("ℹ️ About")

st.sidebar.write(
    """
This ML system predicts Lagos rental prices based on
real property listing data.

Use cases:
- Real estate agencies
- Property investors
- Lagos renters
- Market analysis
"""
)

st.sidebar.markdown("---")

st.sidebar.write(
    """
📡 Market Insight:

Rental prices in Lagos are heavily influenced by:
- Location
- Property size
- Luxury level
- Serviced features
- Neighborhood demand
"""
)

# --------------------------------
# User Inputs
# --------------------------------
st.subheader("📥 Property Information")

Bedrooms = st.slider("Bedrooms", 1, 10, 3)

Neighboorhood = st.selectbox(
    "Neighborhood",
    [
        'Ajah', 'Ikoyi', 'Yaba', 'Surulere', 'Alapere',
        'Shomolu', 'Ilupeju', 'Lekki', 'Amuwo-Odofin',
        'Kosofe', 'Gbagada', 'Ikeja', 'Isolo', 'Ojo',
        'VGC', 'Ikorodu', 'Mushin', 'VI', 'Ogudu',
        'Maryland', 'Bariga', 'Sangotedo', 'Obalende',
        'Apapa', 'Alimosho', 'Ogba', 'Okota', 'Idimu',
        'Agege', 'Ikosi', 'Abule-Egba', 'Ibeju-Lekki',
        'Ipaja', 'Igando', 'Orile', 'Lagos-Island',
        'Oshodi', 'Badagry', 'Ejigbo', 'Ifako-Ijaiye'
    ]
)

Property_Type = st.selectbox(
    "Property Type",
    [
        "1 bedroom mini flat Flat / Apartment",
        "2 bedroom Flat / Apartment",
        "3 bedroom Flat / Apartment",
        "4 bedroom Duplex",
        "5 bedroom Duplex",
        "Self Contain",
        "Office Space"
    ]
)

Furnished = st.selectbox("Furnished", [0, 1])

Serviced = st.selectbox("Serviced", [0, 1])

Luxury = st.selectbox("Luxury", [0, 1])

New_Building = st.selectbox("New Building", [0, 1])

# --------------------------------
# Prediction
# --------------------------------
if st.button("Predict Rent"):

    input_data = {
        "Bedrooms": Bedrooms,
        "Neighboorhood": Neighboorhood,
        "Property_Type": Property_Type,
        "Furnished": Furnished,
        "Serviced": Serviced,
        "Luxury": Luxury,
        "New_Building": New_Building
    }

    prediction = make_prediction(
        model,
        columns,
        input_data
    )

    st.markdown("---")

    # --------------------------------
    # Prediction Output
    # --------------------------------
    st.success(
        f"💰 Estimated Rent Price: ₦{prediction:,.0f}"
    )

    st.metric(
        "Estimated Annual Rent",
        f"₦{prediction:,.0f}"
    )

    st.caption(
        "Estimated annual rent price based on Lagos market patterns."
    )

    # --------------------------------
    # Market Insight
    # --------------------------------
    if prediction > 10000000:
        st.error("⚠️ This property falls within Lagos premium luxury market.")
        st.warning("🔥 Premium Lagos Property Market")

    elif prediction > 3000000:
        st.warning("📈 Mid-high income rental segment.")
        st.info("🏙 Mid-High Rental Market")

    else:
        st.success("🏘 Affordable rental category.")
        st.success("🏡 Affordable Rental Segment")

    # --------------------------------
    # ML Insight
    # --------------------------------
    st.caption(
        "Prediction generated using Random Forest Machine Learning model trained on Lagos rental data."
    )


# --------------------------------
# Analytics Dashboard
# --------------------------------
st.markdown("---")

st.header("📊 Lagos Rental Market Analytics")

# --------------------------------
# Average Rent by Neighborhood
# --------------------------------
st.subheader("🏘 Average Rent by Neighborhood")

avg_rent = (
    df.groupby("Neighboorhood")["Price"]
    .mean()
    .sort_values(ascending=False)
    .head(10)
)

fig1, ax1 = plt.subplots(figsize=(10, 5))

avg_rent.plot(kind="bar", ax=ax1)

ax1.set_ylabel("Average Rent Price")
ax1.set_xlabel("Neighborhood")

st.pyplot(fig1)

# --------------------------------
# Most Common Property Types
# --------------------------------
st.subheader("🏠 Most Common Property Types")

property_counts = (
    df["Property_Type"]
    .value_counts()
    .head(10)
)

fig2, ax2 = plt.subplots(figsize=(10, 5))

property_counts.plot(kind="bar", ax=ax2)

ax2.set_ylabel("Count")
ax2.set_xlabel("Property Type")

st.pyplot(fig2)

# --------------------------------
# Bedroom Distribution
# --------------------------------
st.subheader("🛏 Bedroom Distribution")

bedroom_counts = (
    df["Bedrooms"]
    .value_counts()
    .sort_index()
)

fig3, ax3 = plt.subplots(figsize=(10, 5))

bedroom_counts.plot(kind="bar", ax=ax3)

ax3.set_ylabel("Number of Properties")
ax3.set_xlabel("Bedrooms")

st.pyplot(fig3)

# --------------------------------
# Footer
# --------------------------------
st.markdown("---")

st.caption(
    "Built by Gbolahan | Lagos Real Estate Intelligence Project 🚀"
)