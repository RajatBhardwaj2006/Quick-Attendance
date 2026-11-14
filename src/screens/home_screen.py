from pathlib import Path
import streamlit as st
from src.components.header import header_home
ASSETS = Path(__file__).resolve().parents[1] / "assets"

def _card(role, title, desc, image):
    with st.container(border=True):
        p = ASSETS / image
        if p.exists(): st.image(str(p), width=105)
        st.subheader(title)
        st.write(desc)
        a,b = st.columns(2)
        with a:
            if st.button("Login", key=f"{role}_login", type="primary", use_container_width=True):
                st.session_state.page=f"{role}_login"; st.rerun()
        with b:
            if st.button("Register", key=f"{role}_register", use_container_width=True):
                st.session_state.page=f"{role}_register"; st.rerun()

def home_screen():
    header_home()
    st.markdown("<div class='hero-copy'><span>QUICK ATTENDANCE</span><h1>Attendance, made simple.</h1><p>Choose your portal to continue.</p></div>", unsafe_allow_html=True)
    c1,c2=st.columns(2,gap="large")
    with c1: _card("teacher","Teacher Portal","Create subjects, manage students and record attendance.","teacher.png")
    with c2: _card("student","Student Portal","Join classes and view your attendance history.","student.png")
