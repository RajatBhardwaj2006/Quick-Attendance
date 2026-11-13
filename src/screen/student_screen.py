import streamlit as st

from src.components.header import header_dashboard


def student_screen():
    left, right = st.columns([4, 1], vertical_alignment="center")
    with left:
        header_dashboard()
    with right:
        if st.button("Back to Home", type="secondary", use_container_width=True):
            st.session_state["login_type"] = None
            st.rerun()

    st.divider()
    _, center, _ = st.columns([1, 2, 1])
    with center:
        with st.container(border=True):
            st.subheader("Student portal")
            st.caption("Student login and attendance view can be added here.")
            st.info("This screen is a placeholder. The visual redesign does not add authentication or attendance features.")
