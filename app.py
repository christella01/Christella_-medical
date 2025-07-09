import streamlit as st

# Moved diagnose() function here
def diagnose(symptoms):
    if "fever" in symptoms and "cough" in symptoms:
        return "You may have the flu."
    elif "headache" in symptoms and "nausea" in symptoms:
        return "Possible migraine."
    elif "fatigue" in symptoms and "sore throat" in symptoms:
        return "You may have a viral infection."
    else:
        return "Further tests or a doctor's consultation is recommended."

# Streamlit app
st.title("AI Medical Assistant")

symptoms = st.multiselect(
    "Select patient symptoms:",
    ["fever", "cough", "headache", "nausea", "fatigue", "sore throat"]
)

if st.button("Diagnose"):
    if symptoms:
        result = diagnose(symptoms)
        st.success(f"Diagnosis: {result}")
    else:
        st.warning("Please select at least one symptom.")
