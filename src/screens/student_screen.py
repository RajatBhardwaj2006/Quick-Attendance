import streamlit as st
import pandas as pd
from src.components.header import header_dashboard
from src.database.db import enroll_student, student_subjects, attendance_for_student, save_embedding
from src.pipelines.face_pipeline import extract_face_embedding
from src.pipelines.voice_pipeline import extract_voice_embedding

def student_screen():
    u=st.session_state.user
    a,b=st.columns([4,1],vertical_alignment="center")
    with a: header_dashboard()
    with b:
        if st.button("Logout",use_container_width=True):
            st.session_state.user=None; st.session_state.role=None; st.session_state.page="home"; st.rerun()
    st.title(f"Welcome, {u.get('name','Student')}")
    join,subjects,history,biometrics=st.tabs(["Join subject","My subjects","Attendance history","Biometric enrollment"])
    with join:
        code=st.text_input("Enter subject joining code")
        if st.button("Join class",type="primary"):
            try: enroll_student(u["student_id"],code); st.success("Enrolled successfully.")
            except Exception as e: st.error(f"Enrollment failed: {e}")
    with subjects:
        rows=student_subjects(u["student_id"])
        if rows: st.dataframe(pd.DataFrame(rows),use_container_width=True,hide_index=True)
        else: st.info("You have not joined any subjects yet.")
    with history:
        rows=attendance_for_student(u["student_id"])
        if rows: st.dataframe(pd.DataFrame(rows),use_container_width=True,hide_index=True)
        else: st.info("No attendance records yet.")
    with biometrics:
        st.warning("Only upload your own biometric sample with informed consent. These embeddings are sensitive personal data.")
        face=st.file_uploader("Upload a clear face photo",type=["jpg","jpeg","png"],key="student_face")
        if st.button("Register face",key="save_face"):
            if not face: st.warning("Choose a photo first.")
            else:
                try:
                    emb=extract_face_embedding(face)
                    save_embedding("student",u["student_id"],"face",emb)
                    st.success("Face embedding saved.")
                except Exception as e: st.error(str(e))
        audio=st.file_uploader("Upload a voice sample (WAV)",type=["wav"],key="student_voice")
        if st.button("Register voice",key="save_voice"):
            if not audio: st.warning("Choose a WAV recording first.")
            else:
                try:
                    emb=extract_voice_embedding(audio)
                    save_embedding("student",u["student_id"],"voice",emb)
                    st.success("Voice embedding saved.")
                except Exception as e: st.error(str(e))
