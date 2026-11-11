import streamlit as st


def style_background_home():
    st.markdown("""
        <style>
            .stApp {
                background: #5858F2 !important;
            }

            .stApp div[data-testid="stColumn"] > div {
                background: white !important;
                border-radius: 5rem !important;
                padding: 2rem !important;
            }

            [data-testid="stColumn"] h1,
            [data-testid="stColumn"] h2,
            [data-testid="stColumn"] h3 {
                color: black !important;
            }
        </style>
    """, unsafe_allow_html=True)


def style_background_dashboard():
    st.markdown("""
        <style>
            .stApp {
                background: #E0E3FF !important;
            }
        </style>
    """, unsafe_allow_html=True)
    

def style_base_layout():
    st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Gravitas+One&display=swap');
            @import url('https://fonts.googleapis.com/css2?family=Archivo+Black&display=swap');

            #MainMenu, footer, header {
                visibility: hidden;
            }

            .block-container {
                padding-top: 2.5rem !important;
            }

            h1 {
                font-family: 'Gravitas One', sans-serif !important;
                font-size: 2.5rem !important;
                line-height: 1.1 !important;
                margin-bottom: 0rem !important;
                color: #E0E3FF !important;
            }

            h2 {
                font-family: 'Gravitas One', sans-serif !important;
                font-size: 2.5rem !important;
                line-height: 1.1 !important;
                margin-bottom: 0rem !important;
                color: #E0E3FF !important;
            }

            h3, h4, p {
                font-family: 'Archivo Black', sans-serif;
                font-size: 1.3rem !important;
            }

            button[kind='primary'] {
                border-radius: 1.5rem !important;
                background: #5865F2 !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
            }

            button[kind='primary'] * {
                color: white !important;
            }

            button[kind='secondary'] {
                border-radius: 1.5rem !important;
                background: #EB459E !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
            }

            button[kind='secondary'] * {
                color: white !important;
            }

            button[kind='tertiary'] {
                border-radius: 1.5rem !important;
                background: #EB459E !important;
                color: white !important;
                padding: 10px 20px !important;
                border: none !important;
                transition: transform 0.25s ease-in-out !important;
            }

            button[kind='tertiary'] * {
                color: white !important;
            }

        </style>
    """, unsafe_allow_html=True)
