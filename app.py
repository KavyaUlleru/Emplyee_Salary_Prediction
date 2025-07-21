import streamlit as st
import pickle
import numpy as np

st.title("Employee Salary Predictor")

exp = st.slider("Years of Experience", 0, 20)
edu = st.selectbox("Education Level", ["Bachelors", "Masters", "PhD"])
job = st.selectbox("Job Title", ["Software Engineer", "Data Scientist", "HR Manager"])
loc = st.selectbox("Location", ["New York", "San Francisco", "Chicago"])

input_data = np.array([[exp, {"Bachelors": 0, "Masters": 1, "PhD": 2}[edu],
                        {"Software Engineer": 0, "Data Scientist": 1, "HR Manager": 2}[job],
                        {"New York": 0, "San Francisco": 1, "Chicago": 2}[loc]]])

model = pickle.load(open("model.pkl", "rb"))
prediction = model.predict(input_data)
st.success(f"Predicted Salary: ${prediction[0]:,.2f}")

