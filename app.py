import streamlit as st
from src.ui.base_layout import apply_base_style
from src.screens.home_screen import home_screen
from src.screens.auth_screen import auth_screen
from src.screens.teacher_screen import teacher_screen
from src.screens.student_screen import student_screen
from src.database.db import get_profile_by_id

st.set_page_config(page_title="Quick Attendance", page_icon="📋", layout="wide")

def main():
    apply_base_style()
    for key, value in {"user": None, "role": None, "page": "home"}.items():
        st.session_state.setdefault(key, value)

    if st.session_state.user:
        # Re-check profile on each app session to avoid trusting stale UI state.
        role = st.session_state.role

        user_id = (
            st.session_state.user["teacher_id"]
            if role == "teacher"
            else st.session_state.user["student_id"]
        )

        profile = get_profile_by_id(user_id, role)
        if not profile:
            st.session_state.clear()
            st.rerun()
        st.session_state.user = profile
        if st.session_state.role == "teacher":
            teacher_screen()
        else:
            student_screen()
    elif st.session_state.page in ("teacher_login", "teacher_register", "student_login", "student_register"):
        auth_screen()
    else:
        home_screen()

if __name__ == "__main__":
    main()
