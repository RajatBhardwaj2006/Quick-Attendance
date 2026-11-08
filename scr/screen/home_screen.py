from scr.components.header import header_home
from ui.base_layout import style_base_home
from ui.base_layout import style_base_dashboard
from ui.base_layout import style_base_layout
import streamlit as st


def home_screen():
    header_home()

    style_base_home()
    style_base_dashboard()
    style_base_layout()

    col1, col2 = st.columns(2)

    with col1:
        if st.button("Teacher Portal", key="teacher_portal"):
            st.session_state["login_type"] = "teacher"
            st.rerun()

    with col2:
        if st.button("Student Portal", key="student_portal"):
            st.session_state["login_type"] = "student"
            st.rerun()
