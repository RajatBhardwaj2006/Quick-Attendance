import streamlit as st
from src.components.header import header_dashboard
from src.database.db import register_user, login_user

def auth_screen():
    page=st.session_state.page
    role="teacher" if page.startswith("teacher") else "student"
    registering=page.endswith("register")
    left,right=st.columns([4,1],vertical_alignment="center")
    with left: header_dashboard()
    with right:
        if st.button("Back home", key="auth_home"):
            st.session_state.page="home"; st.rerun()
    st.divider()
    _,mid,_=st.columns([1,1.5,1])
    with mid:
        with st.container(border=True):
            st.subheader(("Create " if registering else "") + role.title() + " account" if registering else role.title()+" login")
            if registering:
                name=st.text_input("Full name")
                email=st.text_input("Email")
                username=st.text_input("Username")
                password=st.text_input("Password",type="password")
                confirm=st.text_input("Confirm password",type="password")
                if st.button("Create account",type="primary",use_container_width=True):
                    if not all([name.strip(),email.strip(),username.strip(),password,confirm]):
                        st.warning("Complete all fields.")
                    elif password != confirm:
                        st.error("Passwords do not match.")
                    elif len(password)<8:
                        st.warning("Use at least 8 characters for your password.")
                    else:
                        try:
                            user=register_user(role,name,email,username,password)
                            if user:
                                st.success("Account created. Please log in.")
                                st.session_state.page=f"{role}_login"; st.rerun()
                        except Exception as e: st.error(f"Registration failed: {e}")
            else:
                username=st.text_input("Username")
                password=st.text_input("Password",type="password")
                if st.button("Login",type="primary",use_container_width=True):
                    try:
                        user=login_user(role,username,password)
                        if user:
                            st.session_state.user=user
                            st.session_state.role=role
                            st.session_state.page="app"
                            st.rerun()
                        st.error("Incorrect username or password.")
                    except Exception as e: st.error(f"Login failed: {e}")
            st.divider()
            if st.button("Switch to "+("login" if registering else "register"),use_container_width=True):
                st.session_state.page=f"{role}_{'login' if registering else 'register'}"; st.rerun()
