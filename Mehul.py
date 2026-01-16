import streamlit as st
from pathlib import Path
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

tile_images = [
    "images/IMG2.jpeg",
    "images/IMG3.jpeg",
    "images/IMG4.jpeg",
    "images/IMG5.jpeg",
    "images/IMG6.jpeg",
    "images/IMG8.jpeg",
    "images/IMG9.jpeg",
    "images/IMG10.jpeg",
]

# Create CSS background using multiple images
bg_css = ", ".join([f'url("{img}")' for img in tile_images])

# -------------------------------------------------
# BACKGROUND TILE CSS
# -------------------------------------------------
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: {bg_css};
        background-size: 250px 250px;
        background-repeat: repeat;
        animation: fadeIn 1.2s ease-in-out;
    }}

    @keyframes fadeIn {{
        from {{ opacity: 0.2; }}
        to {{ opacity: 1; }}
    }}

    .card {{
        background: rgba(255,255,255,0.92);
        padding: 25px;
        border-radius: 15px;
        max-width: 900px;
        margin: auto;
        box-shadow: 0 8px 25px rgba(0,0,0,0.3);
    }}

    /* 📱 Mobile */
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

# -------------------------------------------------
# ADDRESS
# -------------------------------------------------
st.markdown("### 🏡 Home Address")
st.markdown("""
Flat No. A-412, Manglam Anchal  
Kalwar Road, Jhotwara  
Jaipur, Rajasthan – 302012  
""")

st.divider()

# -------------------------------------------------
# EDUCATION
# -------------------------------------------------
st.markdown("### 🏫 Education")
st.markdown("""
School Name: JPHS, Chitrakoot  
Board: CBSE  
Class: 4th-C  
""")

st.divider()

# -------------------------------------------------
# CONTACT
# -------------------------------------------------
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
    w, h = A4

    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(w / 2, h - 50, "Mehul Yadav – Personal Profile")

    c.setFont("Helvetica", 12)
    y = h - 100

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

st.download_button(
    "📄 Download Profile PDF",
    data=generate_pdf(),
    file_name="Mehul_Yadav_Profile.pdf",
    mime="application/pdf"
)

# -------------------------------------------------
# FOOTER
# -------------------------------------------------
st.caption("Tiled Image Background | Shareable Profile Page | Streamlit Cloud Ready")
