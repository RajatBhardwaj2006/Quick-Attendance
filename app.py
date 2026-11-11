
import streamlit as st
from scr.screen.home_screen import home_screen
from scr.screen.student_screen import student_screen
from scr.screen.teacher_screen import teacher_screen


def main():
    if "login_type" not in st.session_state:
        st.session_state["login_type"] = None

    match st.session_state["login_type"]:
        case "teacher":
            teacher_screen()

        case "student":
            student_screen()

        case _:
            home_screen()


if __name__ == "__main__":
    main()

