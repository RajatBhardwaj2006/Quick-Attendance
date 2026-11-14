# QuickAttendance

QuickAttendance is a smart classroom attendance management application built with **Streamlit** and **Supabase (PostgreSQL)**, featuring clean responsive UI styling, role-based access for teachers and students, and modular adapters for optional biometric recognition.

---

## 🚀 Project Overview

QuickAttendance simplifies attendance workflows for educational institutions. Teachers can create subjects, share join codes with students, conduct attendance sessions (manual, face recognition, or voice recognition), and review attendance records. Students can enroll in courses using join codes, view their enrolled subjects, monitor attendance history, and enroll biometric profiles with explicit consent.

### Key Features
- **Teacher & Student Portals:** Secure account registration and authentication using bcrypt password hashing.
- **Course & Subject Management:** Teachers can create subjects with auto-generated unique joining codes.
- **Student Enrollment:** Students enroll in subjects directly using join codes.
- **Attendance Sessions:** Teachers can initiate sessions and record attendance manually or using biometric verification.
- **Records & Analytics:** Instant attendance history inspection for both students and instructors.
- **Optional Biometric Adapters:** Modular face (`face_recognition`) and voice (`resemblyzer`) embedding extraction pipelines.
- **Companion Landing Page:** Lightweight Flask landing site showcasing the application.

---

## 🛠️ Technology Stack

- **Frontend / Application Framework:** [Streamlit](https://streamlit.io/)
- **Database & Storage:** [Supabase](https://supabase.com/) (PostgreSQL with Row Level Security)
- **Authentication & Security:** Bcrypt (`bcrypt`), Python Secrets
- **Data Handling:** Pandas, Pillow
- **Machine Learning (Optional):** NumPy, `face-recognition`, `resemblyzer`, `soundfile`
- **Landing Page:** Flask

---

## 📂 Project Structure

```text
QuickAttendance/
├── .streamlit/
│   ├── config.toml               # Streamlit theme & server configuration
│   └── secrets.toml.example      # Template for Supabase credentials (never commit secrets.toml)
├── landing/                      # Lightweight Flask landing page
│   ├── app.py
│   ├── requirements.txt
│   ├── static/css/style.css
│   └── templates/index.html
├── sql/
│   └── schema.sql                # Supabase PostgreSQL database schema with RLS
├── src/
│   ├── assets/                   # UI graphics and brand illustrations
│   │   ├── logo.png
│   │   ├── student.png
│   │   └── teacher.png
│   ├── components/               # Reusable UI components
│   │   └── header.py
│   ├── database/                 # Supabase client and query helpers
│   │   ├── config.py
│   │   └── db.py
│   ├── pipelines/                # Modular biometric adapters
│   │   ├── face_pipeline.py
│   │   └── voice_pipeline.py
│   ├── screens/                  # Application views
│   │   ├── auth_screen.py
│   │   ├── home_screen.py
│   │   ├── student_screen.py
│   │   └── teacher_screen.py
│   └── ui/                       # Layout and responsive styling
│       └── base_layout.py
├── .gitignore                    # Comprehensive security and cache ignore rules
├── app.py                        # Streamlit application entry point
├── requirements.txt              # Core project dependencies
├── requirements-ml.txt           # Optional machine learning dependencies
└── README.md                     # Project documentation
```

---

## ⚙️ Setup and Installation

### 1. Supabase Database Configuration

1. Create a project at [supabase.com](https://supabase.com/).
2. Open the **SQL Editor** in the Supabase Dashboard.
3. Run the SQL script from `sql/schema.sql` to generate required tables, indices, and enable Row Level Security (RLS).
4. Navigate to **Project Settings → API** to locate your Project URL and service/secret key.
5. Create your local secrets file by copying the template:
   ```powershell
   Copy-Item .streamlit\secrets.toml.example .streamlit\secrets.toml
   ```
6. Open `.streamlit/secrets.toml` and configure your credentials:
   ```toml
   SUPABASE_URL = "https://YOUR_PROJECT_ID.supabase.co"
   SUPABASE_SECRET_KEY = "YOUR_SUPABASE_SECRET_KEY"
   ```
   > [!IMPORTANT]
   > Never commit `.streamlit/secrets.toml` to Git. Keep your secret and service-role keys local and private at all times.

### 2. Local Environment Setup (Windows PowerShell)

```powershell
# Create and activate virtual environment
python -m venv .venv
.\.venv\Scripts\Activate.ps1

# Install core dependencies
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

# Run the QuickAttendance application
streamlit run app.py
```

### 3. Optional Machine Learning Setup

To enable face and voice recognition adapters:
```powershell
python -m pip install -r requirements-ml.txt
```
*Note: `face-recognition` relies on `dlib` which may require C++ build tools on Windows. The core application functions fully without these optional packages.*

### 4. Running the Landing Page (Optional)

The standalone landing page is located in `landing/`:
```powershell
pip install -r landing/requirements.txt
python landing/app.py
```
By default, it will be accessible at `http://localhost:5000` and links to the Streamlit app at `http://localhost:8501`.

---

## 🔒 Security & Privacy Notice

> [!WARNING]
> - **Biometric Privacy:** Student facial photographs, voice recordings, and biometric vector embeddings are sensitive personal data. They must never be published, committed to version control, or stored without explicit informed consent and appropriate security compliance.
> - **Credential Protection:** Database connection credentials, Supabase keys, API tokens, and environment secrets must remain private and excluded from Git history via `.gitignore`.
> - **Test / Dummy Data:** Only use mock or synthetic data for testing. Never push real student records or attendance logs to public repositories.
