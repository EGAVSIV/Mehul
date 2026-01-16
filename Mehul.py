import streamlit as st
from pathlib import Path
from streamlit_autorefresh import st_autorefresh

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="Mehul Yadav Page",
    page_icon="🧾",
    layout="wide"
)

# -------------------------------------------------
# IMAGE PATHS
# -------------------------------------------------
profile_img = Path("images/IMG1.jpeg")

bg_images = [
    "images/IMG2.jpeg",
    "images/IMG3.jpeg",
    "images/IMG4.jpeg",
    "images/IMG5.jpeg",
    "images/IMG6.jpeg",
    "images/IMG7.jpeg",
    "images/IMG8.jpeg",
    "images/IMG9.jpeg",
    "images/IMG10.jpeg",
]

# -------------------------------------------------
# BACKGROUND SLIDESHOW STATE
# -------------------------------------------------
if "bg_index" not in st.session_state:
    st.session_state.bg_index = 0

bg_img = bg_images[st.session_state.bg_index % len(bg_images)]
st.session_state.bg_index += 1

# Auto refresh every 4 seconds (SAFE METHOD)
st_autorefresh(interval=4000, key="bg_refresh")

# -------------------------------------------------
# BACKGROUND CSS
# -------------------------------------------------
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("{bg_img}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
    }}
    .card {{
        background: rgba(255, 255, 255, 0.88);
        padding: 25px;
        border-radius: 15px;
        max-width: 900px;
        margin: auto;
        box-shadow: 0 8px 20px rgba(0,0,0,0.2);
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# -------------------------------------------------
# PROFILE CARD
# -------------------------------------------------
st.markdown('<div class="card">', unsafe_allow_html=True)

st.markdown(
    "<h2 style='text-align:center;'>🧾 Mehul Yadav – Personal Profile</h2>",
    unsafe_allow_html=True
)

col1, col2 = st.columns([1, 2])

with col1:
    if profile_img.exists():
        st.image(str(profile_img), width=180, caption="Mehul Yadav")
    else:
        st.warning("⚠ Profile image not found")

with col2:
    st.markdown("""
**Full Name:** Mehul Yadav  
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
District: Jaipur  
State: Rajasthan  
PIN Code: 302012  
""")

st.divider()

# -------------------------------------------------
# EDUCATION
# -------------------------------------------------
st.markdown("### 🏫 Education")
st.markdown("""
School Name: JPHS, Chitrakoot  
Board: CBSE  
Qualification: 4th-C  
""")

st.divider()

# -------------------------------------------------
# CONTACT
# -------------------------------------------------
st.markdown("### 📞 Contact")
st.markdown("""
Mobile: 9829004534  
Email: yadav.gauravsingh@gmail.com  
""")

st.markdown("</div>", unsafe_allow_html=True)

# -------------------------------------------------
# FOOTER
# -------------------------------------------------
st.caption("Shareable Profile Page | Built with Streamlit")
