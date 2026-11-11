from scr.components.header import header_home
from scr.ui.base_layout import style_background_home
from scr.ui.base_layout import style_background_dashboard
from scr.ui.base_layout import style_base_layout
import streamlit as st


def home_screen():
    header_home()

    style_background_home()
    style_base_layout()

    col1, col2 = st.columns(2, gap="large")

    with col1:
        st.header("I'm Teacher")
        st.image('X:\\VScode\\Artificial_intelligence_n_Machine_learning\\QuickAttendance\\Images\\teacher_image.png',width=150)
        if st.button("Teacher Portal", type='primary', icon=':material/forward:',icon_position="right"):
            st.session_state["login_type"] = "teacher"
            st.rerun()

    with col2:
        st.header("I'm Student")
        st.image('X:\\VScode\\Artificial_intelligence_n_Machine_learning\\QuickAttendance\\Images\\student_image.png',width=130)
        if st.button("Student Portal", type='primary', icon=':material/forward:',icon_position="right"):
            st.session_state["login_type"] = "student"
            st.rerun()
