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
# PROFILE DATA (MULTIPLE PAGES)
# -------------------------------------------------
profiles = {
    "Mehul Yadav": {
        "photo": "images/IMG7.jpeg",
        "email": "mehul19823.20@jphschool.com"
    },
    "Friend Profile": {
        "photo": "images/IMG8.jpeg",
        "email": "friend@email.com"
    }
}

selected_profile = st.sidebar.selectbox("👤 Select Profile", profiles.keys())
profile_img = Path(profiles[selected_profile]["photo"])
email = profiles[selected_profile]["email"]

# -------------------------------------------------
# TILE BACKGROUND IMAGES
# -------------------------------------------------
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

bg_css = ", ".join([f'url("{img}")' for img in tile_images])

# -------------------------------------------------
# BACKGROUND TILE CSS (BLUR + B&W + HOVER ZOOM)
# -------------------------------------------------
st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: {bg_css};
        background-size: 240px 240px;
        background-repeat: repeat;
        filter: grayscale(100%);
    }}

    .stApp::before {{
        content: "";
        position: fixed;
        inset: 0;
        backdrop-filter: blur(6px);
        z-index: -1;
    }}

    .card {{
        background: linear-gradient(135deg, #ffffff, #e8f0ff);
        padding: 30px;
        border-radius: 18px;
        max-width: 900px;
        margin: auto;
        box-shadow: 0 10px 30px rgba(0,0,0,0.35);
        animation: fadeIn 1s ease-in-out;
    }}

    @keyframes fadeIn {{
        from {{ opacity: 0; transform: translateY(10px); }}
        to {{ opacity: 1; transform: translateY(0); }}
    }}

    img {{
        transition: transform 0.4s ease;
    }}

    img:hover {{
        transform: scale(1.08);
    }}

    @media (max-width: 768px) {{
        .card {{
            padding: 20px;
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
    f"<h2 style='text-align:center;'>🧾 {selected_profile} – Personal Profile</h2>",
    unsafe_allow_html=True
)

col1, col2 = st.columns([1, 2])

with col1:
    if profile_img.exists():
        st.image(str(profile_img), width=170, caption=selected_profile)

with col2:
    st.markdown(f"""
**Full Name:** {selected_profile}  
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
st.markdown(f"""
Mobile: 9829004534  
Email: {email}  
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
    c.drawCentredString(w / 2, h - 50, f"{selected_profile} – Personal Profile")

    c.setFont("Helvetica", 12)
    y = h - 100

    lines = [
        f"Name: {selected_profile}",
        "Gender: Male",
        "Blood Group: O+",
        "Nationality: Indian",
        "",
        "Address:",
        "Flat No. A-412, Manglam Anchal",
        "Kalwar Road, Jhotwara",
        "Jaipur – 302012",
        "",
        "Education:",
        "JPHS, Chitrakoot (CBSE)",
        "Class: 4th-C",
        "",
        "Contact:",
        f"Email: {email}",
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
    file_name=f"{selected_profile.replace(' ', '_')}_Profile.pdf",
    mime="application/pdf"
)

# -------------------------------------------------
# FOOTER
# -------------------------------------------------
st.caption("Blurred Tile Background • Multi Profile • Streamlit Cloud Ready")
