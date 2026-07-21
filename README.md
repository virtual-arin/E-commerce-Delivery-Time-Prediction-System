# E-Commerce Delivery Time Prediction System 🚚

---

## 🚌 Business Domain

Logistics and Supply Chain

---

## 🤔 Problem Statement 

In the e-commerce industry, setting accurate delivery expectations is critical. Inaccurate Estimated Time of Arrival (ETA) calculations lead to customer frustration, a high volume of support tickets, and inefficient supply chain management. 

By predicting delivery duration accurately, the company can:
* **Improve Customer Satisfaction:** Provide transparent and reliable delivery timelines.
* **Reduce Late-Delivery Complaints:** Proactively manage bottlenecks before they impact the user.
* **Optimize Logistics Planning:** Enable warehouse and courier operations to better allocate resources.
* **Enhance Seller Performance Monitoring:** Hold regional fulfillment centers and partners accountable.
* **Lower Operational Costs:** Minimize customer support overhead and expensive emergency shipping corrections.

---

## 🎯 Project Objective

The objective of this project is to develop a machine learning regression model that predicts the **expected delivery time (in days)** for an e-commerce order after it has been placed. The model leverages spatial, temporal, transactional, and product characteristics to provide reliable predictions.

---

## 📊 Dataset Overview

* **Source:** [Brazilian E-Commerce Public Dataset by Olist](https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce) on Kaggle.
* **Description:** The dataset contains real, anonymized commercial data from 100k orders made between 2016 and 2018 across various marketplaces in Brazil. It links multiple operational dimensions including customer location, product attributes, seller location, payment types, and detailed tracking timestamps.

---

## 🛠️ Tech Stack

* **Language:** Python
* **Data Manipulation:** NumPy, Pandas
* **Data Visualization:** Matplotlib, Seaborn
* **Machine Learning:** Scikit-Learn
* **Model Storage:** Joblib
* **Environment:** Jupyter Notebook / VS Code

---


## 📂 Project Structure

```text
├── data/
│   ├── raw_data.csv                  # Merged transactional records
│   ├── analysed_data.csv             # Cleaned datasets post-EDA
│   └── processed_data.csv            # Final feature-engineered matrix
├── model/
│   └── delivery_time_model.pkl       # Saved Champion Gradient Boosting Model
├── notebooks/
│   ├── 1.Data Preparation.ipynb      # Ingestion and consolidation pipeline
│   ├── 2.Data Analysis.ipynb         # Statistical EDA and visualization
│   ├── 3.Feature Engineering.ipynb   # Mathematical & logical transform pipeline
│   └── 4.Model Training & Evaluation.ipynb # Training, validation, and serialization
├── src_data/                         # Directory for raw downloaded Olist CSVs
└── README.md                         # Project documentation
└── app.py                            # Streamlit app
```

---

## 🔄 End-to-End Workflow & Approach

### 1. Data Preparation & Merging
* Consolidated 8 distinct relational tables (`customers`, `orders`, `order_items`, `products`, `sellers`, `payments`, `geolocation`, `category_translation`) using standardized relational joins.
* Identified target feature (`delivery_time_days`) by calculating the delta between order purchase and final delivery timestamps.
* Dropped highly sparse, redundant, or leaky future-looking features to prevent data leakage.

### 2. Exploratory Data Analysis (EDA)
* Analyzed distributions of numerical features like freight price, item price, and product dimensions.
* Investigated relationship strengths using regression plots (`sns.regplot`) against the target delivery time.
* Handled missing values and identified outliers across logistical tracking dimensions.

### 3. Feature Engineering
Created advanced interaction features to encapsulate domain dynamics:
* **Logistical Deltas:** `approval_hours` and `carrier_handover_hours` to isolate process bottlenecks.
* **Temporal Fields:** Extracted `purchase_month` and `purchase_dayofweek` to capture seasonality and weekend lags.
* **Geospatial Insights:** Derived a `distance` estimation and a boolean `same_state` indicator comparing customer and seller regions.
* **Physical Attributes:** Engineered `product_volume`, `product_density`, and combined `package_size`.
* **Financial Metrics:** Created `freight_ratio` to capture the relative cost burden of logistics against item base costs.

### 4. Model Training & Evaluation
* Split processed data cleanly into training and testing sets.
* Trained and evaluated multiple predictive algorithms to establish robust baselines:
    * Linear Regression (Baseline)
    * K-Nearest Neighbors (KNN)
    * Decision Tree Regressor
    * Random Forest Regressor
    * Gradient Boosting Regressor (Champion Model)
* **Champion Model Selection:** Saved the fine-tuned Gradient Boosting model (`delivery_time_model.pkl`) using `joblib` for future inference deployment due to its superior $R^2$ performance.

---

## 📈 Results Summary

The evaluated models were ranked primarily based on their Coefficient of Determination ($R^2$ Score) on unseen test data:

| Model | $R^2$ Score | Status |
| :--- | :--- | :--- |
| **Gradient Boosting** | **Highest Performance** | 🏆 *Selected Champion* |
| Random Forest | Competitive | Candidate |
| KNN | Moderate | Baseline |
| Decision Tree | Moderate | Baseline |
| Linear Regression | Lowest Performance | Baseline |

---
   
## 💼 Business Impact

If this model is integrated into an e-commerce platform, it can help the business in several ways:

* **More accurate delivery estimates** so customers know when to expect their orders.
* **Higher customer satisfaction** by reducing unexpected delivery delays.
* **Fewer customer support requests** related to "Where is my order?" because customers receive more reliable ETA(Estimated Time of Arrival.).
* **Better logistics planning** by identifying orders that are likely to take longer and allowing teams to plan shipments more efficiently.
* **Improved seller performance monitoring** by comparing predicted and actual delivery times to identify consistently delayed sellers or regions.
* **Lower operational costs** by reducing emergency shipping, manual interventions, and support workload.

### 👨‍👩‍👧‍👦 Business Outcomes

If deployed in a real e-commerce system, the solution could contribute to:

* More reliable delivery time predictions for every order.
* Reduced late-delivery complaints.
* Faster logistics decision-making.
* Improved customer trust and retention.
* Better resource utilization across warehouses and delivery partners.
