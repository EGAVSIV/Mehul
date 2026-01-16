import streamlit as st
from pathlib import Path
import random
from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas

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
profile_img = Path("images/IMG7.jpeg")

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
# SESSION STATE
# -------------------------------------------------
if "bg_img" not in st.session_state:
    st.session_state.bg_img = random.choice(bg_images)

# -------------------------------------------------
# BUTTONS
# -------------------------------------------------
col_btn1, col_btn2 = st.columns(2)

with col_btn1:
    if st.button("🔁 Random Background"):
        st.session_state.bg_img = random.choice(bg_images)

# -------------------------------------------------
# BACKGROUND + FADE ANIMATION + MOBILE CSS
# -------------------------------------------------
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("{st.session_state.bg_img}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        animation: fadeIn 1.2s ease-in-out;
    }}

    @keyframes fadeIn {{
        from {{ opacity: 0.3; }}
        to {{ opacity: 1; }}
    }}

    .card {{
        background: rgba(255,255,255,0.9);
        padding: 25px;
        border-radius: 15px;
        max-width: 900px;
        margin: auto;
        box-shadow: 0 8px 20px rgba(0,0,0,0.25);
    }}

    /* 📱 Mobile Layout */
    @media (max-width: 768px) {{
        .card {{
            padding: 18px;
            margin: 10px;
        }}
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
        st.image(str(profile_img), width=160, caption="Mehul Yadav")

with col2:
    st.markdown("""
**Full Name:** Mehul Yadav  
**Gender:** Male  
**Blood Group:** O+  
**Nationality:** Indian  
""")

st.divider()

st.markdown("### 🏡 Home Address")
st.markdown("""
Flat No. A-412, Manglam Anchal  
Kalwar Road, Jhotwara  
Jaipur, Rajasthan – 302012  
""")

st.divider()

st.markdown("### 🏫 Education")
st.markdown("""
School Name: JPHS, Chitrakoot  
Board: CBSE  
Class: 4th-C  
""")

st.divider()

st.markdown("### 📞 Contact")
st.markdown("""
Mobile: 9829004534  
Email: mehul19823.20@jphschool.com  
""")

st.markdown("</div>", unsafe_allow_html=True)

# -------------------------------------------------
# PDF GENERATION
# -------------------------------------------------
def generate_pdf():
    buffer = BytesIO()
    c = canvas.Canvas(buffer, pagesize=A4)
    width, height = A4

    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(width / 2, height - 50, "Mehul Yadav – Personal Profile")

    c.setFont("Helvetica", 12)
    y = height - 100

    lines = [
        "Full Name: Mehul Yadav",
        "Gender: Male",
        "Blood Group: O+",
        "Nationality: Indian",
        "",
        "Address:",
        "Flat No. A-412, Manglam Anchal",
        "Kalwar Road, Jhotwara",
        "Jaipur, Rajasthan – 302012",
        "",
        "Education:",
        "JPHS, Chitrakoot (CBSE)",
        "Class: 4th-C",
        "",
        "Contact:",
        "Mobile: 9829004534",
        "Email: mehul19823.20@jphschool.com",
    ]

    for line in lines:
        c.drawString(60, y, line)
        y -= 18

    c.showPage()
    c.save()
    buffer.seek(0)
    return buffer

pdf_bytes = generate_pdf()

with col_btn2:
    st.download_button(
        "📄 Download PDF",
        data=pdf_bytes,
        file_name="Mehul_Yadav_Profile.pdf",
        mime="application/pdf"
    )

# -------------------------------------------------
# FOOTER
# -------------------------------------------------
st.caption("Shareable Profile Page | Mobile Friendly | Streamlit Cloud Ready")
