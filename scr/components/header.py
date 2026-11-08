import streamlit as st
def header_home():
    logo_url = "logo.png"

    st.markdown(f"""
        <div style="display:flex; flex-direction:column; align-items:center; margin-bottom:30px;">
            <img src="{logo_url}" style="height:100px;">
            <h1 style="text-align:center; color:#D4AF37;">QuickAttendance</h1>
        </div>
    """, unsafe_allow_html=True)


def header_dashboard():
    logo_url = "logo.png"

    st.markdown(f"""
        <div style="display:flex; align-items:center; justify-content:center; margin-bottom:30px;">
            <img src="{logo_url}" style="height:65px; margin-right:15px;">
            <h2 style="color:#D4AF37;">QuickAttendance</h2>
        </div>
    """, unsafe_allow_html=True)