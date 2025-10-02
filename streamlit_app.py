import streamlit as st
import pandas as pd
from datetime import datetime

# ---- App Title ----
st.title("COVID-19 Vaccination Screening Questionnaire (Australia)")

st.write("Please complete this short form to check if you are ready for your COVID-19 vaccination.")

# ---- Personal Details ----
st.header("Personal Details")
name = st.text_input("Full Name")
dob = st.date_input("Date of Birth")
address = st.text_area("Address")
phone = st.text_input("Phone Number")
email = st.text_input("Email Address")

# ---- Carer Details (Optional) ----
st.header("Carer (Optional)")
carer_name = st.text_input("Carer's Full Name", "")
carer_phone = st.text_input("Carer's Phone", "")
carer_email = st.text_input("Carer's Email", "")

# ---- Screening Questions ----
st.header("Screening Questions")

q1 = st.radio("Are you feeling well today?", ["Yes", "No"])
q2 = st.radio("Have you had a COVID-19 vaccine before?", ["Yes", "No"])
q3 = st.radio("Have you ever had a severe allergic reaction (anaphylaxis) to a vaccine or medicine?", ["Yes", "No"])
q4 = st.radio("Do you have a bleeding disorder or take blood-thinning medication?", ["Yes", "No"])
q5 = st.radio("Are you pregnant, breastfeeding, or planning pregnancy?", ["Yes", "No"])
q6 = st.radio("Have you tested positive to COVID-19 in the past 6 months?", ["Yes", "No"])
q7 = st.radio("Have you had another vaccine in the past 7 days?", ["Yes", "No"])
q8 = st.radio("Do you have a weakened immune system (e.g. illness or treatment)?", ["Yes", "No"])
q9 = st.radio("Have you ever fainted after a vaccine or injection?", ["Yes", "No"])

# ---- Consent ----
consent = st.checkbox("I consent to receiving the COVID-19 vaccine today")

# ---- Submit Button ----
if st.button("Submit"):
    data = {
        "Name": name,
        "DOB": dob,
        "Address": address,
        "Phone": phone,
        "Email": email,
        "Carer Name": carer_name,
        "Carer Phone": carer_phone,
        "Carer Email": carer_email,
        "Feeling Well": q1,
        "Had COVID Vaccine Before": q2,
        "Severe Allergy": q3,
        "Bleeding Disorder": q4,
        "Pregnant/Breastfeeding": q5,
        "COVID+ in 6 months": q6,
        "Other Vaccine in 7 days": q7,
        "Immunocompromised": q8,
        "Fainting History": q9,
        "Consent": consent,
        "Timestamp": datetime.now()
    }
    
    # Save responses (append to CSV for backend use)
    df = pd.DataFrame([data])
    df.to_csv("responses.csv", mode="a", header=False, index=False)

    # Logic: If no "red flags", show ✅
    if (q1 == "Yes" and q3 == "No" and consent):
        st.success("✅ You are safe to proceed with vaccination")
    else:
        st.error("⚠️ Please speak to a healthcare professional before vaccination.")
