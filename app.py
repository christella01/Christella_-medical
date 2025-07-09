import streamlit as st
from components.diagnosis_engine import get_diagnosis

st.set_page_config(page_title="AI Medical Assistant", layout="centered")

st.title("🩺 AI Medical Assistant")

st.subheader("Enter Patient Information")

name = st.text_input("Patient Name")
age = st.number_input("Patient Age", min_value=0)
symptoms = st.text_area("Symptoms", help="Enter symptoms separated by commas")

if st.button("Analyze"):
    if name and symptoms:
        diagnosis, recommendation = get_diagnosis(symptoms)
        st.success(f"Diagnosis for {name} (Age {age}): {diagnosis}")
        st.info(f"Recommendation: {recommendation}")
    else:
        st.warning("Please enter both name and symptoms.")

