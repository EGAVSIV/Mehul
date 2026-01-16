import streamlit as st

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="Yadav DB – Home",
    page_icon="🏠",
    layout="centered"
)

# -------------------------------------------------
# HEADER
# -------------------------------------------------
st.title("🏠 Yadav DB")
st.subheader("Personal Information Dashboard")
st.divider()

# -------------------------------------------------
# BASIC DETAILS
# -------------------------------------------------
st.markdown("### 👤 Personal Details")

col1, col2 = st.columns(2)

with col1:
    st.text_input("Full Name", value="Yadav")
    st.text_input("Blood Group", value="O+")
    st.text_input("Mobile Number", value="+91 XXXXX XXXXX")

with col2:
    st.text_input("Date of Birth", value="DD-MM-YYYY")
    st.text_input("Email ID", value="example@email.com")
    st.text_input("Gender", value="Male")

# -------------------------------------------------
# EDUCATION DETAILS
# -------------------------------------------------
st.divider()
st.markdown("### 🏫 School Details")

st.text_input("School Name", value="ABC Senior Secondary School")
st.text_input("Board", value="CBSE")
st.text_input("Class / Standard", value="—")

# -------------------------------------------------
# ADDRESS DETAILS
# -------------------------------------------------
st.divider()
st.markdown("### 🏡 Home Address")

st.text_area(
    "Complete Address",
    value="House No, Street Name, Village/City, District, State, PIN Code",
    height=100
)

# -------------------------------------------------
# EMERGENCY DETAILS
# -------------------------------------------------
st.divider()
st.markdown("### 🚑 Emergency Information")

col3, col4 = st.columns(2)

with col3:
    st.text_input("Emergency Contact Name", value="—")

with col4:
    st.text_input("Emergency Contact Number", value="+91 XXXXX XXXXX")

# -------------------------------------------------
# FOOTER
# -------------------------------------------------
st.divider()
st.caption("📌 Yadav DB | Secure Personal Records | Streamlit App")
