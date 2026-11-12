import streamlit as st
from src.components.header import header_dashboard
from src.ui.base_layout import style_background_dashboard, style_base_layout

def teacher_screen():
    style_background_dashboard()
    style_base_layout()

    c1, c2 = st.columns([3, 1], vertical_alignment='center', gap='medium')    
    with c1:
        header_dashboard()
    with c2:
        st.markdown('<div style="display: flex; justify-content: flex-end;">', unsafe_allow_html=True)
        if st.button("back to Home", type='secondary', key='loginbackbtn', shortcut="control+backspace"):
            st.session_state["login_type"] = None
            st.rerun()
        st.markdown('</div>', unsafe_allow_html=True)
    # st.header('Register your teacher Profile')
    st.markdown('<h2 style="color: #000000 !important; font-family: \'Gravitas One\', sans-serif;">Register your teacher Profile.</h2>', unsafe_allow_html=True)
