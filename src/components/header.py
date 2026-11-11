
import streamlit as st
import base64

def header_home():
    logo_path = r"X:\VScode\Artificial_intelligence_n_Machine_learning\QuickAttendance\Images\QuickAttendanceLogo.png"

    with open(logo_path, "rb") as image_file:
        encoded_image = base64.b64encode(image_file.read()).decode()

    st.markdown(f"""
        <div style="display: flex; flex-direction: column; align-items: center; justify-content: center; margin-bottom: 30px; margin-top: 30px">
            <img src="data:image/png;base64,{encoded_image}" style="height: 150px; width: auto; object-fit: contain;"/>
            <h1 style="text-align: center; color: #E0E3FF; font-size: 7rem; margin: 0;">Quick</br>Attendance</h1>
        </div>
    """, unsafe_allow_html=True)