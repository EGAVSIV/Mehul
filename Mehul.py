import streamlit as st

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="Yadav DB – D Form",
    page_icon="📄",
    layout="centered"
)

# -------------------------------------------------
# HEADER
# -------------------------------------------------
st.markdown(
    """
    <h2 style="text-align:center;">📄 D FORM – PERSONAL DETAILS</h2>
    <hr>
    """,
    unsafe_allow_html=True
)

# -------------------------------------------------
# PHOTO + BASIC INFO
# -------------------------------------------------
col1, col2 = st.columns([1, 2])

with col1:
    st.image("assets/photo.jpg", width=160, caption="Photograph")

with col2:
    st.markdown("""
    **Full Name:** Yadav Singh  
    **Father’s Name:** Ram Singh Yadav  
    **Date of Birth:** 12-05-1995  
    **Gender:** Male  
    **Blood Group:** O+  
    **Nationality:** Indian  
    """)

st.divider()

# -------------------------------------------------
# ADDRESS DETAILS
# -------------------------------------------------
st.markdown("### 🏡 Permanent Address")

st.markdown("""
House No: 21  
Village: Rampur  
District: Jaipur  
State: Rajasthan  
PIN Code: 302012  
""")

st.divider()

# -------------------------------------------------
# EDUCATION DETAILS
# -------------------------------------------------
st.markdown("### 🏫 Educational Details")

st.markdown("""
**School Name:** ABC Senior Secondary School  
**Board:** CBSE  
**Highest Qualification:** 12th Pass  
""")

st.divider()

# -------------------------------------------------
# EMERGENCY DETAILS
# -------------------------------------------------
st.markdown("### 🚑 Emergency Contact")

st.markdown("""
**Contact Name:** Suresh Yadav  
**Relation:** Brother  
**Mobile:** +91 80039 94518  
""")

st.divider()

# -------------------------------------------------
# DECLARATION
# -------------------------------------------------
st.markdown("### 📌 Declaration")

st.markdown("""
I hereby declare that the above information is true and correct to the best of my knowledge.
""")

st.markdown("<br>", unsafe_allow_html=True)

# -------------------------------------------------
# SIGNATURE
# -------------------------------------------------
col3, col4 = st.columns(2)

with col3:
    st.markdown("**Place:** Jaipur")

with col4:
    st.markdown("**Signature:** ____________")

st.markdown("<hr>", unsafe_allow_html=True)

# -------------------------------------------------
# FOOTER
# -------------------------------------------------
st.caption("Yadav DB | Official Record | Streamlit Cloud Ready")
