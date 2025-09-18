import streamlit as st
import numpy as np

st.write("fixed width text")
st.set_page_config(page_title="CKD", page_icon ="👩‍⚕️")
import pickle

with open("chronic_kidney(1).pkl","rb") as file:
    rf_random = pickle.load(file)

st.title("Chronic Kidney Disease Prediction App 🩺")
st.write("Enter patient details below to predict risk:")


age = st.number_input("Age", min_value=2.0, max_value=90.0, value=45.0, step=1.0)
blood_pressure = st.number_input("Blood_Pressure", min_value=66.6, max_value=155.2, value=80.0, step=0.1)
specific_gravity = st.number_input("Specific_Gravity", min_value=1.005, max_value=1.025, value=1.015, step=0.001)
albumin = st.number_input("Albumin", min_value=0.0, max_value=5.0, value=1.0, step=0.1)
sugar = st.number_input("Sugar", min_value=0.0, max_value=5.0, value=1.0, step=0.1)
blood_glucose_random = st.number_input("Blood_Glucose_Random", min_value=50.0, max_value=373.2, value=120.0, step=1.0)
blood_urea = st.number_input("Blood Urea", min_value=5.0, max_value=135.6, value=40.0, step=0.1)
serum_creatinine = st.number_input("Serum_Creatinine", min_value=0.30, max_value=7.82, value=1.2, step=0.01)
sodium = st.number_input("Sodium", min_value=120.0, max_value=155.0, value=140.0, step=0.1)
potassium = st.number_input("Potassium", min_value=2.50, max_value=7.10, value=4.5, step=0.01)
hemoglobin = st.number_input("Hemoglobin", min_value=6.0, max_value=20.0, value=13.0, step=0.1)
packed_cell_volume = st.number_input("Packed_Cell_Volume", min_value=25.0, max_value=55.0, value=40.0, step=1.0)
white_blood_cell_count = st.number_input("White_Blood_Cell_Count", min_value=3000, max_value=18000, value=8000, step=100)
red_blood_cell_count = st.number_input("Red_Blood_Cell_Count", min_value=3.0, max_value=7.5, value=5.0, step=0.1)


gender = st.radio("Gender", ["Male", "Female"])
gender = 1 if gender == "Male" else 0

pus_cell = st.radio("Pus Cell", ["Normal", "Abnormal"])
pus_cell = 0 if pus_cell == "Normal" else 1

pus_cell_clumps = st.radio("Pus Cell Clumps", ["Not Present", "Present"])
pus_cell_clumps = 0 if pus_cell_clumps == "Not Present" else 1

bacteria = st.radio("Bacteria", ["Not Present", "Present"])
bacteria = 0 if bacteria == "Not Present" else 1

hypertension = st.radio("Hypertension", ["No", "Yes"])
hypertension = 1 if hypertension == "Yes" else 0

diabetes_mellitus = st.radio("Diabetes Mellitus", ["No", "Yes"])
diabetes_mellitus = 1 if diabetes_mellitus == "Yes" else 0

coronary_artery_disease = st.radio("Coronary Artery Disease", ["No", "Yes"])
coronary_artery_disease = 1 if coronary_artery_disease == "Yes" else 0

appetite = st.radio("Appetite", ["Good", "Poor"])
appetite = 1 if appetite == "Good" else 0

anemia = st.radio("Anemia", ["No", "Yes"])
anemia = 1 if anemia == "Yes" else 0

pedal_edema = st.radio("Pedal Edema", ["No", "Yes"])
pedal_edema = 1 if pedal_edema == "Yes" else 0

user_input = np.array([[
    gender, pus_cell, pus_cell_clumps, bacteria, hypertension,
    diabetes_mellitus, coronary_artery_disease, appetite, anemia, pedal_edema,
    age, blood_pressure, specific_gravity, albumin, sugar,
    blood_glucose_random, blood_urea, serum_creatinine, sodium, potassium,
    hemoglobin, packed_cell_volume, white_blood_cell_count, red_blood_cell_count
]])
if st.button("Predict CKD"):
    prediction = rf_random.predict(user_input)[0]
    if prediction == 1:
        st.error("⚠️ The model predicts that the patient **has CKD**.")
    else:
        st.success("✅ The model predicts that the patient **does not have CKD**.")




    


