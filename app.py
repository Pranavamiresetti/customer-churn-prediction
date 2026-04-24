import streamlit as st
import pickle
import numpy as np

model = pickle.load(open("model.pkl", "rb"))

st.title("Customer Churn Prediction")

tenure = st.number_input("Tenure", min_value=0)
monthly_charges = st.number_input("Monthly Charges", min_value=0.0)

if st.button("Predict"):

    input_data = np.zeros((1, model.n_features_in_))

    input_data[0][0] = tenure
    input_data[0][1] = monthly_charges

    prediction = model.predict(input_data)

    if prediction[0] == 1:
        st.error("Customer is likely to churn")
    else:
        st.success("Customer will stay")
