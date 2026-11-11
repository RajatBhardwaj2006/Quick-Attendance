# QuickAttendance 📸

### AI-Powered Smart Attendance Management System

QuickAttendance is an AI/ML-powered attendance management system that automates classroom attendance using computer vision and facial recognition.

Instead of manually calling student names, teachers can simply upload a photograph of the classroom. The system analyzes the image, identifies enrolled students, and automatically generates an attendance record.

## 🚀 Project Overview

Traditional attendance systems are time-consuming and require teachers to manually verify each student's presence.

QuickAttendance aims to simplify this process through Machine Learning and Computer Vision.

**How it works:**
1. Teacher logs into the platform.
2. Teacher selects the class and uploads a classroom photograph.
3. The system detects and recognizes students in the photograph.
4. Identified students are marked as Present.
5. Students who are not detected are flagged for teacher verification before being marked Absent.
6. Teacher reviews and confirms the attendance record.

## ✨ Key Features

- **Automated Attendance:** Generate attendance records using classroom photographs.
- **Face Detection:** Detect multiple faces within a single classroom image.
- **Face Recognition:** Identify students using previously registered facial data.
- **Attendance Management:** Maintain student-wise attendance records.
- **Teacher Dashboard:** Provide an interface for uploading images and managing attendance.
- **Attendance Verification:** Allow teachers to review and correct automatically generated records.

## 🛠️ Tech Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Machine Learning | Machine Learning, Computer Vision |
| Image Processing | OpenCV |
| Numerical Computing | NumPy |
| Backend | Python / Flask |
| Frontend | HTML, CSS, JavaScript |
| Database | To be finalized |

## 📂 Project Structure

```text
QuickAttendance/
│
├── src/
│   ├── components/
│   ├── screen/
│   └── ui/
│
├── images/
│
├── app.py
├── requirements.txt
└── README.md
```

## ⚙️ Installation & Setup

**1. Clone the repository**

```bash
git clone <repository-url>
```

**2. Navigate to the project directory**

```bash
cd QuickAttendance
```

**3. Create a virtual environment**

```bash
python -m venv venv
```

**4. Activate the virtual environment**

Windows:
```bash
venv\Scripts\activate
```

**5. Install dependencies**

```bash
pip install -r requirements.txt
```

**6. Run the application**

```bash
python app.py
```

## 🔒 Privacy & Security

- Student facial data should be stored securely.
- Access to attendance records should be restricted to authorized users.
- Student images and biometric information should only be processed with appropriate consent.
- Automated attendance results should be reviewed by teachers before final confirmation.

## 🎯 Project Objective

The primary objective of QuickAttendance is to reduce manual attendance-taking efforts, minimize administrative workload, and demonstrate the practical application of Artificial Intelligence and Computer Vision in educational environments.

## 🚧 Project Status

**Development in Progress**

More features and improvements will be introduced as the project develops.

---

*QuickAttendance — Making classroom attendance smarter with AI.*
