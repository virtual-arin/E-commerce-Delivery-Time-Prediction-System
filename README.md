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

## 🧑‍🍳 Data Preparation
* Built a machine-learning-ready E-Commerce Delivery Time dataset by merging 9 relational tables from the Olist Brazilian E-Commerce dataset and creating a delivery_time_days target feature for EDA, data cleaning, feature engineering, and regression modeling.
* **Source** [Brazilian Ecommerce Delivery Time Dataset](https://www.kaggle.com/datasets/virtualarin/e-commerce-delivery-time-dataset)

---

## 🛠️ Tech Stack

* **Language:** Python
* **Data Manipulation:** NumPy, Pandas
* **Data Visualization:** Matplotlib, Seaborn
* **Machine Learning:** Scikit-Learn
* **Model Storage:** Joblib
* **Environment:** Jupyter Notebook / VS Code

---

## 📈 Data Visualization

1. **Visualization of missing values in data**
- Most missing data comes from product category that is around 1.4 percent of total records.
[Missing Values](https://github.com/virtual-arin/E-commerce-Delivery-Time-Prediction-System/blob/main/images/missing_values.png)

2. **How is the delivery time distributed?**
- Delivery times are heavily right-skewed, with the vast majority of orders arriving within ten to twenty days.
[Delivery time](https://github.com/virtual-arin/E-commerce-Delivery-Time-Prediction-System/blob/main/images/delivery_time_distribution.png)

3. **Which order statuses are most common?**
- Almost all orders in the dataset successfully reach the delivered status, with an extremely low cancellation rate.
(Order Status)[https://github.com/virtual-arin/E-commerce-Delivery-Time-Prediction-System/blob/main/images/order_status_distribution.png]

4. **Which product categories have the highest average delivery time?**
- Office furniture takes significantly longer to deliver than other categories, over twenty days per standard order.
[Highest average delivery](https://github.com/virtual-arin/E-commerce-Delivery-Time-Prediction-System/blob/main/images/top_10_slowest_product_delivery.png)

5. **Does freight cost (total fees charged by a carrier to transport goods) increase delivery time?**
- Higher freight costs does not guarantee faster deliveries, as many cheap shipments still experience extensive delays.
[Freight_value_vs_delivery_time](https://github.com/virtual-arin/E-commerce-Delivery-Time-Prediction-System/blob/main/images/freight_value_vs_delivery_time.png)

6. **Does product weight affect delivery time?**
- Product weight shows no strong correlation with delivery time, meaning heavy items do not always arrive slower.
[product_weight_vs_delivery_time](https://github.com/virtual-arin/E-commerce-Delivery-Time-Prediction-System/blob/main/images/product_weight_vs_delivery_time.png)

7. **Which payment method is associated with the longest delivery time?**
- Delivery speeds remained consistent across all payment methods, indicating payment type does not impacts the shipping duration.
[delivery_time_by_payment_status](https://github.com/virtual-arin/E-commerce-Delivery-Time-Prediction-System/blob/main/images/delivery_time_by_payment_status.png)

8. **Which customer states experience the longest average delivery time?**
- Customers located in RR and AP experience the longest average wait times for deliveries.
[top_customer_states_by_delivery_time](https://github.com/virtual-arin/E-commerce-Delivery-Time-Prediction-System/blob/main/images/top_customer_states_by_delivery_time.png)

9. **Which seller states have the longest average delivery time?**
- Orders from AM experienced the highest delivery time
[top_seller_states_by_delivery_time](https://github.com/virtual-arin/E-commerce-Delivery-Time-Prediction-System/blob/main/images/top_seller_states_by_delivery_time.png)

10. **Is there a relationship between price and delivery time?**
- Many cheap items have experienced a high delivery time as compared to expensive price 
[price_vs_delivery_time](https://github.com/virtual-arin/E-commerce-Delivery-Time-Prediction-System/blob/main/images/price_vs_delivery_time.png)

11. **Correlation Heatmap of dataset**

[correlation_heatmap](https://github.com/virtual-arin/E-commerce-Delivery-Time-Prediction-System/blob/main/images/correlation_heatmap.png)
---

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
