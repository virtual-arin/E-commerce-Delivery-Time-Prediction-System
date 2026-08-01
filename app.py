import os
import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import LabelEncoder

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Delivery Time Predictor",
    page_icon="🚚",
    layout="centered"
)

st.title("🚚 E-Commerce Delivery Time Predictor")
st.write("Enter the order details to estimate delivery time in days.")

# ---------------- LOAD MODEL ----------------
MODEL_PATH = "model/delivery_time_model.pkl"

@st.cache_resource
def load_model():
    if os.path.exists(MODEL_PATH):
        return joblib.load(MODEL_PATH)
    return None

model = load_model()

if model is None:
    st.error(f"❌ Model not found at: {MODEL_PATH}")
    st.stop()

# ---------------- CATEGORICAL OPTIONS ----------------
product_categories = [
    "housewares",
    "perfumery",
    "auto",
    "health_beauty",
    "sports_leisure",
    "OTHER"
]

payment_types = [
    "credit_card",
    "boleto",
    "voucher",
    "debit_card"
]

# ---------------- INPUTS ----------------
st.subheader("📦 Product Details")

price = st.number_input("Price ($)", min_value=0.0, value=50.0)
freight_value = st.number_input("Freight Value ($)", min_value=0.0, value=15.0)

product_weight_g = st.number_input("Weight (g)", min_value=0.0, value=500.0)
product_length_cm = st.number_input("Length (cm)", min_value=0.0, value=20.0)
product_height_cm = st.number_input("Height (cm)", min_value=0.0, value=10.0)
product_width_cm = st.number_input("Width (cm)", min_value=0.0, value=15.0)

product_photos_qty = st.number_input("Photos Quantity", min_value=0.0, value=1.0)
product_category = st.selectbox("Product Category", product_categories)

st.subheader("💳 Payment Details")

payment_type = st.selectbox("Payment Type", payment_types)
payment_installments = st.number_input("Payment Installments", min_value=1, max_value=24, value=1)
payment_value = st.number_input("Payment Value ($)", min_value=0.0, value=65.0)

st.subheader("📅 Purchase Details")

purchase_hour = st.slider("Purchase Hour", 0, 23, 12)
purchase_day = st.slider("Purchase Day", 1, 31, 15)
purchase_weekday = st.slider("Purchase Weekday (0=Mon)", 0, 6, 2)
purchase_month = st.slider("Purchase Month", 1, 12, 6)

st.subheader("🚚 Logistics")

same_state = st.checkbox("Customer and Seller are in the same state", value=True)
geo_distance = st.number_input("Geographical Distance", min_value=0.0, value=5.0)

# ---------------- FEATURE ENGINEERING ----------------
product_volume = product_length_cm * product_height_cm * product_width_cm

# ---------------- BUILD INPUT DATA ----------------
input_data = {
    "price": price,
    "freight_value": freight_value,
    "product_name_lenght": 40,
    "product_description_lenght": 200,
    "product_photos_qty": product_photos_qty,
    "product_weight_g": product_weight_g,
    "product_length_cm": product_length_cm,
    "product_height_cm": product_height_cm,
    "product_width_cm": product_width_cm,
    "product_category_name_english": product_category,
    "payment_sequential": 1,
    "payment_type": payment_type,
    "payment_installments": payment_installments,
    "payment_value": payment_value,
    "customer_lat": 0.0,
    "customer_lng": 0.0,
    "seller_lat": 0.0,
    "seller_lng": 0.0,
    "purchase_hour": purchase_hour,
    "purchase_day": purchase_day,
    "purchase_weekday": purchase_weekday,
    "purchase_month": purchase_month,
    "same_state": int(same_state),
    "product_volume": product_volume,
    "geo_distance": geo_distance
}

input_df = pd.DataFrame([input_data])

# ---------------- ENCODE CATEGORICAL FEATURES ----------------
category_encoder = LabelEncoder()
category_encoder.fit(product_categories)
input_df["product_category_name_english"] = category_encoder.transform(
    input_df["product_category_name_english"]
)

payment_encoder = LabelEncoder()
payment_encoder.fit(payment_types)
input_df["payment_type"] = payment_encoder.transform(
    input_df["payment_type"]
)

# ---------------- FEATURE ORDER ----------------
feature_order = [
    'price', 'freight_value', 'product_name_lenght',
    'product_description_lenght', 'product_photos_qty',
    'product_weight_g', 'product_length_cm', 'product_height_cm',
    'product_width_cm', 'product_category_name_english',
    'payment_sequential', 'payment_type', 'payment_installments',
    'payment_value', 'customer_lat', 'customer_lng', 'seller_lat',
    'seller_lng', 'purchase_hour', 'purchase_day',
    'purchase_weekday', 'purchase_month', 'same_state',
    'product_volume', 'geo_distance'
]

input_df = input_df[feature_order]

# ---------------- PREDICTION ----------------
st.divider()

if st.button("🔮 Predict Delivery Time", use_container_width=True):
    try:
        prediction = model.predict(input_df)[0]
        estimated_days = max(0, round(float(prediction), 1))

        st.success(f"### 🎉 Estimated Delivery Time: **{estimated_days} days**")

    except Exception as e:
        st.error(f"❌ Prediction failed: {e}")