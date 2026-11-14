import streamlit as st
def apply_base_style():
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=DM+Sans:wght@400;500;600;700&family=Manrope:wght@600;700;800&display=swap');
    :root{--bg:#F5F7FB;--surface:#fff;--primary:#3157D5;--text:#17233C;--muted:#68758D;--border:#E2E8F0}
    .stApp{background:var(--bg);color:var(--text)}
    html,body,[class*="css"]{font-family:'DM Sans',sans-serif}
    .block-container{max-width:1100px;padding-top:2rem;padding-bottom:3rem}
    h1,h2,h3{font-family:'Manrope',sans-serif!important;color:var(--text)!important}
    p,label,.stCaption{color:var(--muted)}
    .brand-title{font-family:Manrope,sans-serif;font-size:1.55rem;font-weight:800;color:var(--text)}
    .brand-subtitle{font-size:.85rem;color:var(--muted)}
    .brand-mark{width:48px;height:48px;border-radius:12px;background:#E8EEFF;color:var(--primary);display:flex;align-items:center;justify-content:center;font-size:24px;font-weight:800}
    .hero-copy{text-align:center;margin:2.4rem 0 1.5rem}.hero-copy span{font-size:.8rem;font-weight:700;letter-spacing:.12em;color:var(--primary)}
    .hero-copy h1{margin:.35rem 0}.hero-copy p{font-size:1rem}
    div[data-testid="stVerticalBlockBorderWrapper"]{background:var(--surface);border:1px solid var(--border);border-radius:16px}
    div[data-testid="stTextInput"] input{background:#fff;color:var(--text);border:1px solid var(--border);border-radius:10px;min-height:44px}
    div[data-testid="stTextInput"] label{color:var(--text);font-weight:600}
    .stButton>button{border-radius:10px;min-height:42px;font-weight:700}
    .stButton>button[kind="primary"]{background:var(--primary);color:#fff;border:1px solid var(--primary)}
    .stButton>button[kind="primary"] p{color:#fff!important}
    .stButton>button[kind="secondary"]{background:#fff;color:var(--text);border:1px solid var(--border)}
    hr{border-color:var(--border)}
    </style>""",unsafe_allow_html=True)
