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

# New: advice function based on result
def give_advice(diagnosis):
    if "flu" in diagnosis:
        return "Stay hydrated, rest well, and consider antiviral medication if prescribed by a doctor."
    elif "migraine" in diagnosis:
        return "Stay in a quiet, dark room. Take pain relievers and avoid screen time. See a neurologist if it persists."
    elif "viral infection" in diagnosis:
        return "Drink plenty of fluids, rest, and use throat lozenges or warm tea to soothe your throat."
    else:
        return "Please consult with a doctor for further medical evaluation and lab tests."

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

        advice = give_advice(result)
        st.info(f"Advice: {advice}")
    else:
        st.warning("Please select at least one symptom.")

