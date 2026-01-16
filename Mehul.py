import streamlit as st
from pathlib import Path

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="Mehul Yadav Page",
    page_icon="🧾",
    layout="centered"
)

# -------------------------------------------------
# HEADER
# -------------------------------------------------
st.markdown(
    """
    <h2 style="text-align:center;">🧾 Mehul Yadav – Personal Profile</h2>
    <p style="text-align:center;">(Shareable Personal Information Page)</p>
    <hr>
    """,
    unsafe_allow_html=True
)

# -------------------------------------------------
# IMAGE SAFE LOADER
# -------------------------------------------------
img_path = Path("assets/mehul.jpg")

col1, col2 = st.columns([1, 2])

with col1:
    if img_path.exists():
        st.image(str(img_path), width=160, caption="Mehul Yadav")
    else:
        st.warning("⚠ Image not found. Please check file name & path.")

with col2:
    st.markdown("""
**Full Name:** Mehul Yadav  
**Father’s Name:** —  
**Date of Birth:** —  
**Gender:** Male  
**Blood Group:** O+  
**Nationality:** Indian  
""")

st.divider()

# -------------------------------------------------
# ADDRESS
# -------------------------------------------------
st.markdown("### 🏡 Home Address")

st.markdown("""
Village / City: —  
District: —  
State: —  
PIN Code: —  
""")

st.divider()

# -------------------------------------------------
# EDUCATION
# -------------------------------------------------
st.markdown("### 🏫 Education")

st.markdown("""
School Name: —  
Board: —  
Class / Qualification: —  
""")

st.divider()

# -------------------------------------------------
# CONTACT
# -------------------------------------------------
st.markdown("### 📞 Contact Information")

st.markdown("""
Mobile: —  
Email: —  
""")

st.divider()

# -------------------------------------------------
# DECLARATION
# -------------------------------------------------
st.markdown("### 📌 Declaration")

st.markdown("""
This page is created for sharing basic personal information with friends.
""")

st.markdown("<br>", unsafe_allow_html=True)

# -------------------------------------------------
# FOOTER
# -------------------------------------------------
st.caption("Created using Streamlit | Shareable Profile Page")
