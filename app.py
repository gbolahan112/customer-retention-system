import streamlit as st
from src.predict import load_model, make_prediction

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
# Footer
# --------------------------------
st.markdown("---")

st.caption(
    "Built by Gbolahan | Lagos Real Estate Intelligence Project 🚀"
)