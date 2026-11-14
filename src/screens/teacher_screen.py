import streamlit as st
import pandas as pd
from src.components.header import header_dashboard
from src.database.db import (teacher_subjects, create_subject, subject_students,
    subject_student_biometrics, create_attendance_session, mark_attendance, attendance_for_subject)
from src.pipelines.face_pipeline import extract_face_embedding, compare_embeddings as compare_faces
from src.pipelines.voice_pipeline import extract_voice_embedding, compare_embeddings as compare_voices

def _logout():
    st.session_state.user=None; st.session_state.role=None; st.session_state.page="home"; st.rerun()

def teacher_screen():
    u=st.session_state.user
    left,right=st.columns([4,1],vertical_alignment="center")
    with left: header_dashboard()
    with right:
        if st.button("Logout",use_container_width=True): _logout()
    st.title(f"Welcome, {u.get('name','Teacher')}")
    tabs=st.tabs(["My subjects","Create subject","Attendance","Records"])
    subjects=teacher_subjects(u["teacher_id"])
    with tabs[0]:
        if not subjects: st.info("No subjects yet. Create your first subject.")
        for s in subjects:
            with st.container(border=True):
                st.subheader(f"{s['name']} · {s['subject_code']}")
                st.caption(f"Section: {s.get('section','N/A')} | Join code: {s.get('join_code','')}")
                students=subject_students(s["subject_id"])
                st.write(f"Enrolled students: {len(students)}")
                if students: st.dataframe(pd.DataFrame(students),use_container_width=True,hide_index=True)
    with tabs[1]:
        with st.form("create_subject_form"):
            name=st.text_input("Subject name")
            code=st.text_input("Subject code")
            section=st.text_input("Section",value="N/A")
            submitted=st.form_submit_button("Create subject",type="primary")
        if submitted:
            if not name.strip() or not code.strip(): st.warning("Subject name and code are required.")
            else:
                try:
                    s=create_subject(u["teacher_id"],code,name,section)
                    st.success(f"Created. Student joining code: {s['join_code']}")
                    st.rerun()
                except Exception as e: st.error(f"Could not create subject: {e}")
    with tabs[2]:
        if not subjects: st.info("Create a subject first.")
        else:
            labels={f"{s['name']} ({s['subject_code']}) — {s['section']}":s for s in subjects}
            selected=st.selectbox("Choose subject",list(labels))
            subject=labels[selected]
            mode=st.radio("Attendance method",["Manual","Face recognition","Voice recognition"],horizontal=True)
            if mode=="Manual":
                roster=subject_students(subject["subject_id"])
                if st.button("Start manual session",type="primary"):
                    st.session_state.active_session=create_attendance_session(subject["subject_id"],u["teacher_id"],"manual")
                session=st.session_state.get("active_session")
                if session and session["subject_id"]==subject["subject_id"]:
                    for student in roster:
                        present=st.checkbox(student["name"],key=f"manual_{session['id']}_{student['student_id']}")
                        if st.button(f"Save {student['name']}",key=f"manual_save_{session['id']}_{student['student_id']}"):
                            mark_attendance(session["id"],subject["subject_id"],student["student_id"],present,"manual")
                            st.success("Saved.")
            elif mode=="Face recognition":
                photo=st.file_uploader("Upload one student's face photo",type=["jpg","jpeg","png"],key="face_att")
                if st.button("Identify and mark present",type="primary",key="face_mark"):
                    try:
                        query=extract_face_embedding(photo) if photo else None
                        if query is None: st.warning("Upload a photo first.")
                        else:
                            roster=subject_student_biometrics(subject["subject_id"])
                            matches=[x for x in roster if x.get("face_embedding") and compare_faces(query,x["face_embedding"])]
                            if len(matches)==1:
                                session=create_attendance_session(subject["subject_id"],u["teacher_id"],"face")
                                mark_attendance(session["id"],subject["subject_id"],matches[0]["student_id"],True,"face")
                                st.success(f"Matched {matches[0]['name']} and marked present.")
                            elif len(matches)>1: st.error("Ambiguous match. Do not mark automatically.")
                            else: st.warning("No matching enrolled face found.")
                    except Exception as e: st.error(str(e))
            else:
                audio=st.file_uploader("Upload one student's voice recording (WAV)",type=["wav"],key="voice_att")
                if st.button("Identify voice and mark present",type="primary",key="voice_mark"):
                    try:
                        query=extract_voice_embedding(audio) if audio else None
                        if query is None: st.warning("Upload a WAV recording first.")
                        else:
                            roster=subject_student_biometrics(subject["subject_id"])
                            matches=[x for x in roster if x.get("voice_embedding") and compare_voices(query,x["voice_embedding"])]
                            if len(matches)==1:
                                session=create_attendance_session(subject["subject_id"],u["teacher_id"],"voice")
                                mark_attendance(session["id"],subject["subject_id"],matches[0]["student_id"],True,"voice")
                                st.success(f"Matched {matches[0]['name']} and marked present.")
                            elif len(matches)>1: st.error("Ambiguous match. Do not mark automatically.")
                            else: st.warning("No matching voice found.")
                    except Exception as e: st.error(str(e))
                st.caption("This prototype identifies one uploaded speaker sample at a time. It is not a live classroom microphone system.")
    with tabs[3]:
        if not subjects: st.info("No subjects yet.")
        else:
            labels={f"{s['name']} ({s['subject_code']})":s for s in subjects}
            choice=st.selectbox("Records for subject",list(labels),key="record_subject")
            rows=attendance_for_subject(labels[choice]["subject_id"])
            if rows: st.dataframe(pd.DataFrame(rows),use_container_width=True,hide_index=True)
            else: st.info("No attendance records yet.")
