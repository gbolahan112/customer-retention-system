from src.predict import load_model, make_prediction


# Load model
model, columns = load_model()

# Sample property
sample_data = {
    "Bedrooms": 3,
    "Neighboorhood": "Lekki",
    "Property_Type": "3 bedroom Flat / Apartment",
    "Furnished": 1,
    "Serviced": 1,
    "Luxury": 1,
    "New_Building": 1
}

# Predict
prediction = make_prediction(model, columns, sample_data)

print(f"\nEstimated Rent Price: ₦{prediction:,.2f}")