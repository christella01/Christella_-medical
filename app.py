import streamlit as st
from components.diagnosis_engine import diagnose

st.set_page_config(page_title="AI Medical Assistant", layout="centered")

st.title("🩺 AI Medical Assistant")
st.write("Enter the patient's symptoms to get an initial diagnosis and recommendations.")

# Input fields
patient_name = st.text_input("Patient Name")
age = st.number_input("Age", min_value=0, max_value=120, step=1)
symptoms = st.text_area("Describe the symptoms (e.g. fever, cough, headache)")

# Button to analyze
if st.button("Analyze Symptoms"):
    if not symptoms.strip():
        st.warning("Please enter symptoms.")
    else:
        result = diagnose(symptoms)
        st.subheader("Diagnosis Result")
        st.write(result["diagnosis"])
        
        st.subheader("Suggested Recommendations")
        for rec in result["recommendations"]:
            st.write(f"- {rec}")
