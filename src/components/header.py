from pathlib import Path
import streamlit as st
ASSETS=Path(__file__).resolve().parents[1]/"assets"
def _brand(size=48):
    a,b=st.columns([0.12,0.88],vertical_alignment="center",gap="small")
    with a:
        logo=ASSETS/"logo.png"
        if logo.exists(): st.image(str(logo),width=size)
        else: st.markdown("<div class='brand-mark'>Q</div>",unsafe_allow_html=True)
    with b:
        st.markdown("<div class='brand-title'>Quick Attendance</div><div class='brand-subtitle'>Simple attendance management</div>",unsafe_allow_html=True)
def header_home(): _brand()
def header_dashboard(): _brand(44)
