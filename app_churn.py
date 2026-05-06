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
st.info("🚀 ML-powered Customer Retention Tool")
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

st.sidebar.markdown("---")
st.sidebar.write(
    "📡 Use case: Telecom companies (MTN, Airtel, Glo) can use this tool "
    "to identify customers at risk of leaving and take action early."
)

# -------------------------------
# Input Section
# -------------------------------
st.subheader("📥 Customer Information")

SeniorCitizen = st.selectbox("Senior Citizen", [0, 1])
tenure = st.slider("Tenure (months)", 0, 72, 12)
MonthlyCharges = st.number_input("Monthly Charges", min_value=0.0, value=70.5)
TotalCharges = st.number_input("Total Charges", min_value=0.0, value=800.0)

# 🔥 NEW FEATURES (VERY IMPORTANT)
Contract = st.selectbox("Contract Type", ["Month-to-month", "One year", "Two year"])

InternetService = st.selectbox("Internet Service", ["DSL", "Fiber optic", "No"])

PaymentMethod = st.selectbox(
    "Payment Method",
    ["Electronic check", "Mailed check", "Bank transfer (automatic)", "Credit card (automatic)"]
)

PaperlessBilling = st.selectbox("Paperless Billing", ["Yes", "No"])

# -------------------------------
# Prediction
# -------------------------------
if st.button("Predict Churn"):

    input_data = {
        "SeniorCitizen": SeniorCitizen,
        "tenure": tenure,
        "MonthlyCharges": MonthlyCharges,
        "TotalCharges": TotalCharges,
        "Contract": Contract,
        "InternetService": InternetService,
        "PaymentMethod": PaymentMethod,
        "PaperlessBilling": PaperlessBilling
    }

    prediction, probability = make_prediction(model, columns, input_data)

    st.markdown("---")

    # -------------------------------
    # Result Display
    # -------------------------------
    if prediction == 1:
        st.error("🚨 High Risk: Customer likely to churn")
    else:
        st.success("✅ Low Risk: Customer likely to stay")

    # -------------------------------
    # Business Recommendation
    # -------------------------------
    if prediction == 1:
        st.write("💡 Action: Offer discounts, improve support, or engage immediately.")
    else:
        st.write("💡 Action: Maintain current service and monitor behavior.")

    # -------------------------------
    # Probability
    # -------------------------------
    st.write(f"**Churn Probability:** {probability:.2%}")

    # -------------------------------
    # Risk Level
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