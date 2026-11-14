import bcrypt
import secrets
import string
from datetime import datetime, timezone
from src.database.config import get_supabase

def _db():
    return get_supabase()

def _hash(password: str) -> str:
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")

def _verify(password: str, hashed: str) -> bool:
    try:
        return bcrypt.checkpw(password.encode("utf-8"), hashed.encode("utf-8"))
    except (ValueError, TypeError):
        return False

def register_user(role, name, email, username, password):
    table = "teacher" if role == "teacher" else "students"
    row = {
        "name": name.strip(),
        "email": email.strip().lower(),
        "user_name": username.strip().lower(),
        "password_hash": _hash(password),
    }
    result = _db().table(table).insert(row).execute()
    return result.data[0] if result.data else None

def login_user(role, username, password):
    table = "teacher" if role == "teacher" else "students"
    result = (_db().table(table).select("*")
              .eq("user_name", username.strip().lower()).limit(1).execute())
    if not result.data:
        return None
    user = result.data[0]
    if not _verify(password, user.get("password_hash", "")):
        return None
    return {k: v for k, v in user.items() if k != "password_hash"}

def get_profile_by_id(user_id, role):
    table = "teacher" if role == "teacher" else "students"
    result = _db().table(table).select("*").eq("teacher_id" if role=="teacher" else "student_id", user_id).limit(1).execute()
    if not result.data: return None
    return {k:v for k,v in result.data[0].items() if k != "password_hash"}

def create_subject(teacher_id, code, name, section):
    join_code = "".join(secrets.choice(string.ascii_uppercase + string.digits) for _ in range(7))
    result = _db().table("subjects").insert({
        "teacher_id": teacher_id, "subject_code": code.strip().upper(),
        "name": name.strip(), "section": section.strip(), "join_code": join_code
    }).execute()
    return result.data[0] if result.data else None

def teacher_subjects(teacher_id):
    return _db().table("subjects").select("*").eq("teacher_id", teacher_id).order("subject_id", desc=True).execute().data

def student_subjects(student_id):
    rows = _db().table("subject_student").select("subject_id, subjects(*)").eq("student_id", student_id).execute().data
    return [r["subjects"] for r in rows if r.get("subjects")]

def enroll_student(student_id, join_code):
    found = _db().table("subjects").select("subject_id").eq("join_code", join_code.strip().upper()).limit(1).execute().data
    if not found: raise ValueError("No subject found for that joining code.")
    _db().table("subject_student").upsert({
        "subject_id": found[0]["subject_id"], "student_id": student_id
    }, on_conflict="subject_id,student_id").execute()

def subject_students(subject_id):
    rows = (_db().table("subject_student")
            .select("student_id, students(student_id,name,user_name,email)")
            .eq("subject_id", subject_id).execute().data)
    return [r["students"] for r in rows if r.get("students")]

def create_attendance_session(subject_id, teacher_id, method):
    result = _db().table("attendance_sessions").insert({
        "subject_id": subject_id, "teacher_id": teacher_id, "method": method,
        "started_at": datetime.now(timezone.utc).isoformat()
    }).execute()
    return result.data[0]

def mark_attendance(session_id, subject_id, student_id, status, method):
    _db().table("attendance").upsert({
        "session_id": session_id, "subject_id": subject_id, "student_id": student_id,
        "if_present": bool(status), "method": method,
        "timestamp": datetime.now(timezone.utc).isoformat()
    }, on_conflict="session_id,student_id").execute()

def attendance_for_student(student_id):
    return (_db().table("attendance")
            .select("id,timestamp,if_present,method,subjects(name,subject_code)")
            .eq("student_id", student_id).order("timestamp", desc=True).execute().data)

def attendance_for_subject(subject_id):
    return (_db().table("attendance")
            .select("id,timestamp,if_present,method,students(name,user_name)")
            .eq("subject_id", subject_id).order("timestamp", desc=True).execute().data)

def save_embedding(role, user_id, kind, embedding):
    table = "teacher" if role == "teacher" else "students"
    id_col = "teacher_id" if role == "teacher" else "student_id"
    col = "face_embedding" if kind == "face" else "voice_embedding"
    _db().table(table).update({col: embedding}).eq(id_col, user_id).execute()


def subject_student_biometrics(subject_id):
    rows = (_db().table("subject_student")
            .select("student_id, students(student_id,name,user_name,face_embedding,voice_embedding)")
            .eq("subject_id", subject_id).execute().data)
    return [r["students"] for r in rows if r.get("students")]

def get_student_biometrics(student_id):
    result = (_db().table("students")
              .select("face_embedding,voice_embedding")
              .eq("student_id", student_id).limit(1).execute())
    return result.data[0] if result.data else {}
