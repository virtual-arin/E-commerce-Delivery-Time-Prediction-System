import os
import streamlit as st
import pandas as pd
import numpy as np
import joblib
from sklearn.preprocessing import LabelEncoder, StandardScaler

# --- PAGE SETUP ---
st.set_page_config(
    page_title="Delivery Time Prediction App",
    page_icon="🚚",
    layout="centered"
)

st.title("🚚 E-Commerce Delivery Time Predictor")
st.write("Enter the order details below to estimate the delivery time in days.")

# --- LOAD MODEL ---
MODEL_PATH = "model/delivery_time_model.pkl"

@st.cache_resource
def load_model():
    if os.path.exists(MODEL_PATH):
        return joblib.load(MODEL_PATH)
    else:
        st.error(f"Model file not found at `{MODEL_PATH}`. Please train and save your model first!")
        return None

model = load_model()

# Only render the app inputs if the model loaded successfully
if model is not None:
    
    # --- HARDCODED PREPROCESSING MAPS (Based on notebook data) ---
    # In a production app, LabelEncoder instances and StandardScaler should be saved 
    # during training and loaded here. Below are fallback placeholders for UI rendering.
    categorical_options = {
        "order_status": ["delivered", "shipped", "canceled", "invoiced", "processing"],
        "customer_state": ["SP", "BA", "GO", "RJ", "MG", "RS", "PR", "SC", "OTHER"],
        "product_category_name_english": ["housewares", "perfumery", "auto", "health_beauty", "sports_leisure", "OTHER"],
        "seller_state": ["SP", "PR", "MG", "RJ", "SC", "RS", "OTHER"],
        "payment_type": ["credit_card", "boleto", "voucher", "debit_card"]
    }

    st.subheader("Order Configuration")
    
    # --- USER INPUT FIELDS ---
    col1, col2 = st.columns(2)
    
    with col1:
        order_status = st.selectbox("Order Status", categorical_options["order_status"])
        customer_state = st.selectbox("Customer State", categorical_options["customer_state"])
        seller_state = st.selectbox("Seller State", categorical_options["seller_state"])
        product_category = st.selectbox("Product Category", categorical_options["product_category_name_english"])
        payment_type = st.selectbox("Payment Type", categorical_options["payment_type"])
        
        price = st.number_input("Price ($)", min_value=0.0, value=50.0, step=1.0)
        freight_value = st.number_input("Freight Value ($)", min_value=0.0, value=15.0, step=1.0)
        payment_value = st.number_input("Total Payment Value ($)", min_value=0.0, value=65.0, step=1.0)
        payment_installments = st.number_input("Payment Installments", min_value=1, max_value=24, value=1)
        
    with col2:
        product_weight_g = st.number_input("Product Weight (grams)", min_value=0.0, value=500.0, step=50.0)
        product_length_cm = st.number_input("Product Length (cm)", min_value=0.0, value=20.0, step=1.0)
        product_height_cm = st.number_input("Product Height (cm)", min_value=0.0, value=10.0, step=1.0)
        product_width_cm = st.number_input("Product Width (cm)", min_value=0.0, value=15.0, step=1.0)
        product_photos_qty = st.number_input("Product Photos Qty", min_value=0.0, value=1.0, step=1.0)
        
        approval_hours = st.number_input("Approval Hours", min_value=0.0, value=1.0, step=0.5)
        carrier_handover_hours = st.number_input("Carrier Handover Hours", min_value=0.0, value=24.0, step=1.0)
        distance = st.number_input("Distance Metric", min_value=0.0, value=3.5, step=0.1)
        purchase_month = st.slider("Purchase Month", 1, 12, 6)
        purchase_dayofweek = st.slider("Purchase Day of Week (0=Mon, 6=Sun)", 0, 6, 2)

    # --- CALCULATED FEATURES (Mirroring your backend engineered features) ---
    product_volume = product_length_cm * product_height_cm * product_width_cm
    same_state = 1 if customer_state == seller_state else 0
    freight_ratio = freight_value / price if price > 0 else 0
    product_density = product_weight_g / product_volume if product_volume > 0 else 0
    package_size = product_length_cm + product_height_cm + product_width_cm

    # --- CONSTRUCT DATAFRAME ---
    # Essential: Ensure keys match the exact feature order expected by your model (X.columns)
    input_data = {
        "order_status": order_status,
        "customer_state": customer_state,
        "price": price,
        "freight_value": freight_value,
        "product_photos_qty": product_photos_qty,
        "product_weight_g": product_weight_g,
        "product_length_cm": product_length_cm,
        "product_height_cm": product_height_cm,
        "product_width_cm": product_width_cm,
        "product_category_name_english": product_category,
        "seller_state": seller_state,
        "payment_type": payment_type,
        "payment_installments": payment_installments,
        "payment_value": payment_value,
        "approval_hours": approval_hours,
        "carrier_handover_hours": carrier_handover_hours,
        "purchase_month": purchase_month,
        "purchase_dayofweek": purchase_dayofweek,
        "distance": distance,
        "product_volume": product_volume,
        "same_state": same_state,
        "freight_ratio": freight_ratio,
        "product_density": product_density,
        "package_size": package_size
    }
    
    input_df = pd.DataFrame([input_data])

    # --- STREAMLIT MATCHES NOTEBOOK PREPROCESSING ---
    # Note: For production pipelines, you should save the actual LabelEncoder map 
    # used during training using pickle/joblib to avoid encoding drift.
    for col in categorical_options.keys():
        le = LabelEncoder()
        # Mock fit using the predefined categories to prevent crash
        le.fit(categorical_options[col])
        try:
            input_df[col] = le.transform(input_df[col].astype(str))
        except ValueError:
            # Handle unseen test categories gracefully
            input_df[col] = 0 

    # --- PREDICTION BUTTON ---
    st.write("---")
    if st.button("🔮 Predict Delivery Time", type="primary"):
        # Note: Gradient Boosting did NOT use X_train_scaled in your notebook loop, 
        # it was fed raw X_train for training. We will pass the dataframe directly.
        prediction = model.predict(input_df)
        
        # Output formatting
        estimated_days = max(0, round(prediction[0], 1)) # Prevents impossible negative days
        
        st.success(f"### 🎉 Estimated Delivery Time: **{estimated_days} days**")