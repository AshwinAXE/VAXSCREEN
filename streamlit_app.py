import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(page_title="COVID-19 Vaccine Screening", page_icon="💉", layout="centered")

# ---- App Title ----
st.title("💉 COVID-19 Vaccination Screening (Australia)")
st.markdown("Please complete this short form to check if you’re ready for your COVID-19 vaccination.")

# ---- Personal Details ----
st.header("👤 Personal Details")
col1, col2 = st.columns(2)
with col1:
    name = st.text_input("Full Name")
    dob = st.date_input("Date of Birth (DD/MM/YYYY)", format="DD/MM/YYYY")
    phone = st.text_input("Phone Number")
with col2:
    email = st.text_input("Email Address")
    address = st.text_area("Home Address")

# ---- Carer Details (Optional) ----
with st.expander("👥 Add Carer Details (Optional)"):
    carer_name = st.text_input("Carer’s Full Name", "")
    carer_phone = st.text_input("Carer’s Phone", "")
    carer_email = st.text_input("Carer’s Email", "")

st.markdown("---")

# ---- Screening Questions ----
st.header("📝 Screening Questions")

def yesno(label):
    return st.radio(label, ["Yes", "No"], horizontal=True)

q1 = yesno("Are you feeling well today?")
q2 = yesno("Have you had a COVID-19 vaccine before?")
q3 = yesno("Have you ever had a severe allergic reaction (anaphylaxis) to a vaccine or medicine?")
q4 = yesno("Do you have a bleeding disorder or take blood-thinning medication?")
q5 = yesno("Are you pregnant, breastfeeding, or planning pregnancy?")
q6 = yesno("Have you tested positive to COVID-19 in the past 6 months?")
q7 = yesno("Have you had another vaccine in the past 7 days?")
q8 = yesno("Do you have a weakened immune system (e.g. illness or treatment)?")
q9 = yesno("Have you ever fainted after a vaccine or injection?")

st.markdown("---")

# ---- Consent ----
consent = st.checkbox("✅ I consent to receiving the COVID-19 vaccine today")

# ---- Submit Button ----
if st.button("Submit Form", use_container_width=True):
    data = {
        "Name": name,
        "DOB": dob.strftime("%d/%m/%Y"),
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
        "Timestamp": datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
    }

    # Save to CSV (append mode)
    df = pd.DataFrame([data])
    df.to_csv("responses.csv", mode="a", header=not pd.io.common.file_exists("responses.csv"), index=False)

    # ---- Results Display ----
    if (q1 == "Yes" and q3 == "No" and consent):
        st.success("### ✅ You are safe to proceed with vaccination")
        st.balloons()
    else:
        st.error("### ⚠️ Please speak to a healthcare professional before vaccination")
