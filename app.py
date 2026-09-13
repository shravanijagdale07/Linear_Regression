import streamlit as st
import pandas as pd
import pickle

# Load the trained model
with open("model.pkl", "rb") as file:
    model = pickle.load(file)

# Application title
st.title("Student Performance Prediction")

st.write("Enter student details to predict the Performance Index.")

# User inputs
hours_studied = st.number_input("Hours Studied")
previous_scores = st.number_input("Previous Scores")

extracurricular = st.selectbox(
    "Extracurricular Activities",
    ["No", "Yes"]
)

sleep_hours = st.number_input("Sleep Hours")
sample_papers = st.number_input("Sample Question Papers Practiced")

# Prediction
if st.button("Predict Performance Index"):

    # Convert Yes/No into 1/0
    extracurricular_encoded = 1 if extracurricular == "Yes" else 0

    # Create input DataFrame
    input_data = pd.DataFrame([[
        hours_studied,
        previous_scores,
        extracurricular_encoded,
        sleep_hours,
        sample_papers
    ]], columns=[
        "Hours Studied",
        "Previous Scores",
        "Extracurricular Activities",
        "Sleep Hours",
        "Sample Question Papers Practiced"
    ])

    # Predict Performance Index
    prediction = model.predict(input_data)[0]

    # Display result
    st.success(f"Predicted Performance Index: {prediction:.2f}")