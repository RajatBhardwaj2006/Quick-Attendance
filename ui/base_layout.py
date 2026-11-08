import streamlit as st

def style_base_home():
    st.markdown('''
        <style>
            .stApp {
                background: #006039 !important;
            }
        </style>
    ''', unsafe_allow_html=True)


def style_base_dashboard():
    st.markdown('''
        <style>
            .stApp {
                background: #006039 !important;
            }
        </style>
    ''', unsafe_allow_html=True)


def style_base_layout():
    st.markdown('''
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Archivo+Black&family=Outfit:wght@400;500;600;700&display=swap');

            header, #MainMenu, footer {
                display: none !important;
            }

            .block-container {
                padding-top: 1.5rem !important;
            }

            h1, h2 {
                font-family: 'Archivo Black', sans-serif !important;
                color: #D4AF37 !important;
                font-size: 3.5rem !important;
                line-height: 1.1 !important;
                margin-bottom: 0.5rem;
            }

            h3, h4, p {
                font-family: 'Outfit', sans-serif !important;
                color: #F5F3E8 !important;
            }

            button {
                border-radius: 1.5rem !important;
                background: #D4AF37 !important;
                color: #003B29 !important;
                padding: 10px 20px !important;
                border: 1px solid #E4C76B !important;
                transition: transform 0.25s ease-in-out !important;
            }

            button:hover {
                background: #F5D76E !important;
                transform: translateY(-2px);
            }

            input, textarea {
                background: #004D33 !important;
                color: #F5F3E8 !important;
                border: 1px solid #8F7935 !important;
                border-radius: 10px !important;
            }
        </style>
    ''', unsafe_allow_html=True)