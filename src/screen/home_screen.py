from pathlib import Path
import streamlit as st

from src.components.header import header_home

ASSET_DIR = Path(__file__).resolve().parents[1] / "assets"


def _portal_card(title: str, description: str, image_name: str, button_label: str, login_type: str):
    with st.container(border=True):
        image_path = ASSET_DIR / image_name
        if image_path.exists():
            st.image(str(image_path), width=110)
        st.subheader(title)
        st.write(description)
        if st.button(button_label, type="primary", use_container_width=True, key=f"{login_type}_portal"):
            st.session_state["login_type"] = login_type
            if login_type == "teacher":
                st.session_state["teacher_page"] = "login"
            st.rerun()


def home_screen():
    header_home()
    st.write("")
    st.markdown(
        "<div style='text-align:center;margin:2.2rem 0 1.5rem'>"
        "<div style='font-size:0.8rem;font-weight:700;letter-spacing:.12em;"
        "text-transform:uppercase;color:#3157D5'>Welcome</div>"
        "<h1 style='margin:.35rem 0'>Attendance, made simple.</h1>"
        "<p style='font-size:1rem'>Choose how you want to continue.</p></div>",
        unsafe_allow_html=True,
    )

    col1, col2 = st.columns(2, gap="large")
    with col1:
        _portal_card(
            "Teacher Portal",
            "Create and manage sessions and keep track of attendance.",
            "teacher.png",
            "Continue as Teacher",
            "teacher",
        )
    with col2:
        _portal_card(
            "Student Portal",
            "View your attendance and stay updated with your classes.",
            "student.png",
            "Continue as Student",
            "student",
        )
