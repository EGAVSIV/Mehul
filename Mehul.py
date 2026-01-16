import streamlit as st
from pathlib import Path
from io import BytesIO
from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import qrcode

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="Mehul Yadav Page",
    page_icon="🧾",
    layout="wide"
)

# -------------------------------------------------
# DEFAULT PROFILES (ADMIN CAN ADD MORE)
# -------------------------------------------------
if "profiles" not in st.session_state:
    st.session_state.profiles = {
        "Mehul Yadav": {
            "photo": "images/IMG7.jpeg",
            "email": "mehul19823.20@jphschool.com",
            "mobile": "9829004534"
        }
    }

profiles = st.session_state.profiles

# -------------------------------------------------
# SIDEBAR – PROFILE SELECT
# -------------------------------------------------
st.sidebar.title("👤 Profiles")
selected_profile = st.sidebar.selectbox("Select Profile", profiles.keys())

profile = profiles[selected_profile]
profile_img = Path(profile["photo"])

# -------------------------------------------------
# ADMIN PANEL (ADD PROFILE)
# -------------------------------------------------
st.sidebar.divider()
st.sidebar.subheader("🔐 Admin Panel")

with st.sidebar.expander("➕ Add New Profile"):
    name = st.text_input("Name")
    photo = st.text_input("Photo path (images/xxx.jpeg)")
    email = st.text_input("Email")
    mobile = st.text_input("Mobile")

    if st.button("Add Profile"):
        if name:
            profiles[name] = {
                "photo": photo,
                "email": email,
                "mobile": mobile
            }
            st.success("Profile added (session only)")
            st.rerun()

# -------------------------------------------------
# TILE BACKGROUND (BLUR + B/W)
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
    }}

    img {{
        transition: transform 0.4s ease;
    }}

    img:hover {{
        transform: scale(1.08);
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

st.markdown("### 📞 Contact")
st.markdown(f"""
Mobile: {profile["mobile"]}  
Email: {profile["email"]}  
""")

# -------------------------------------------------
# QR CODE PER PROFILE
# -------------------------------------------------
st.subheader("🔳 Share Profile via QR")

profile_url = f"https://share.streamlit.app/{selected_profile.replace(' ', '_')}"
qr = qrcode.make(profile_url)

qr_buf = BytesIO()
qr.save(qr_buf, format="PNG")
qr_buf.seek(0)

st.image(qr_buf, width=150)
st.caption("Scan to open profile")

# -------------------------------------------------
# WHATSAPP SHARE
# -------------------------------------------------
whatsapp_text = f"Check out {selected_profile}'s profile: {profile_url}"
wa_link = f"https://wa.me/?text={whatsapp_text.replace(' ', '%20')}"

st.markdown(f"[📲 Share on WhatsApp]({wa_link})", unsafe_allow_html=True)

# -------------------------------------------------
# PHOTO GALLERY MODAL
# -------------------------------------------------
st.subheader("🖼 Photo Gallery")

with st.expander("Open Gallery"):
    cols = st.columns(3)
    gallery = tile_images + [profile["photo"]]

    for i, img in enumerate(gallery):
        with cols[i % 3]:
            st.image(img, use_container_width=True)

st.markdown("</div>", unsafe_allow_html=True)

# -------------------------------------------------
# PDF DOWNLOAD
# -------------------------------------------------
def generate_pdf():
    buf = BytesIO()
    c = canvas.Canvas(buf, pagesize=A4)
    w, h = A4

    c.setFont("Helvetica-Bold", 16)
    c.drawCentredString(w / 2, h - 50, f"{selected_profile} – Personal Profile")

    c.setFont("Helvetica", 12)
    y = h - 100

    lines = [
        f"Name: {selected_profile}",
        f"Mobile: {profile['mobile']}",
        f"Email: {profile['email']}",
    ]

    for line in lines:
        c.drawString(60, y, line)
        y -= 20

    c.showPage()
    c.save()
    buf.seek(0)
    return buf

st.download_button(
    "📄 Download Profile PDF",
    data=generate_pdf(),
    file_name=f"{selected_profile.replace(' ', '_')}_Profile.pdf",
    mime="application/pdf"
)

# -------------------------------------------------
# FOOTER
# -------------------------------------------------
st.caption("QR • WhatsApp • Admin Panel • Gallery | Streamlit Cloud Ready")
