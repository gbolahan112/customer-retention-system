import streamlit as st
from src.predict import load_model, make_prediction

# -------------------------------
# Page Config
# -------------------------------
st.set_page_config(
    page_title="Customer Churn Predictor",
    page_icon="📊",
    layout="centered"
)

# -------------------------------
# Load Model
# -------------------------------
@st.cache_resource
def load():
    return load_model()

model, columns = load()

# -------------------------------
# Header
# -------------------------------
st.title("📊 Customer Churn Prediction App")
st.markdown("### Predict if a customer will churn using Machine Learning")

st.markdown("---")

# -------------------------------
# Sidebar
# -------------------------------
st.sidebar.header("ℹ️ About")
st.sidebar.write(
    "This app predicts whether a customer will churn using a trained machine learning model. "
    "It helps businesses identify high-risk customers early and take action."
)

# -------------------------------
# Input Section
# -------------------------------
st.subheader("📥 Customer Information")

SeniorCitizen = st.selectbox("Senior Citizen", [0, 1])
tenure = st.slider("Tenure (months)", 0, 72, 12)
MonthlyCharges = st.number_input("Monthly Charges", min_value=0.0, value=70.5)
TotalCharges = st.number_input("Total Charges", min_value=0.0, value=800.0)

# -------------------------------
# Prediction
# -------------------------------
if st.button("Predict Churn"):

    input_data = {
        "SeniorCitizen": SeniorCitizen,
        "tenure": tenure,
        "MonthlyCharges": MonthlyCharges,
        "TotalCharges": TotalCharges
    }

    prediction, probability = make_prediction(model, columns, input_data)

    st.markdown("---")

    # -------------------------------
    # Result Display
    # -------------------------------
    if prediction == 1:
        st.error("⚠️ Customer is likely to churn")
    else:
        st.success("✅ Customer is likely to stay")

    # -------------------------------
    # Probability
    # -------------------------------
    st.write(f"**Churn Probability:** {probability:.2%}")

    # -------------------------------
    # Risk Level (🔥 important)
    # -------------------------------
    if probability > 0.6:
        st.error("High Risk 🚨")
        st.write("💡 Recommended action: Offer incentives or support immediately.")
    elif probability > 0.3:
        st.warning("Medium Risk ⚠️")
        st.write("💡 Monitor customer behavior and improve engagement.")
    else:
        st.success("Low Risk ✅")
        st.write("💡 Customer is stable. Maintain current service quality.")

# -------------------------------
# Footer
# -------------------------------
st.markdown("---")
st.caption("Built by Gbolahan | Machine Learning Pipeline 🚀")