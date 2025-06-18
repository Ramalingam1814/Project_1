import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open('salary_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Streamlit UI
st.set_page_config(page_title="Salary Prediction App", layout="centered")

st.title("?? Salary Prediction System")
st.write("Enter the employee details to predict their estimated salary.")

# Input form
age = st.number_input("Age", min_value=18, max_value=65, value=30)
gender = st.selectbox("Gender", ["Male", "Female"])
education = st.selectbox("Education Level", ["Bachelor's", "Master's", "PhD"])
experience = st.slider("Years of Experience", 0, 40, 5)

# Encode categorical data as per your model
gender_encoded = 1 if gender == "Female" else 0
education_encoded = {
    "Bachelor's": 1,
    "Master's": 0,
    "PhD": 2
}[education]

# Predict button
if st.button("Predict Salary"):
    input_data = np.array([[age, gender_encoded, education_encoded, experience]])
    prediction = model.predict(input_data)
    st.success(f"?? Predicted Salary: ?{prediction[0]:,.2f}")
