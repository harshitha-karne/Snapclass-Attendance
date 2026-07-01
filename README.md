# SnapClass Attendance

SnapClass Attendance is an AI-powered attendance management system that makes classroom attendance faster, smarter, and easier. It allows teachers to manage subjects, enroll students, and mark attendance using face recognition or voice recognition.

## Live Project

- **Live App:** [https://snapclass-attendance2026.streamlit.app/](https://snapclass-attendance2026.streamlit.app/)
- **Landing Page:** [https://snap-class-landing-page-six.vercel.app](https://snap-class-landing-page-six.vercel.app)

## About The Project

Traditional attendance marking takes time and can be inefficient in large classrooms. SnapClass solves this by using AI-based face and voice recognition to automate attendance.

The system has two main portals:

- **Teacher Portal:** Teachers can create subjects, share class codes, take attendance, and view attendance records.
- **Student Portal:** Students can register using Face ID, optionally enroll their voice, join subjects, and track their attendance.

## Features

### Teacher Features

- Teacher registration and login
- Create and manage subjects
- Generate subject codes
- Share subject join links and QR codes
- Upload classroom photos for face-based attendance
- Record classroom audio for voice-based attendance
- View attendance history and summaries

### Student Features

- Student login using Face ID
- New student profile creation
- Face enrollment during registration
- Optional voice enrollment
- Join subjects using subject codes
- View enrolled subjects
- Track attendance records
- Unenroll from subjects

### AI Features

- Face recognition using dlib and face embeddings
- Student classification using machine learning
- Voice recognition using speaker embeddings
- Automatic attendance marking
- Bulk attendance from classroom photos or audio

## Tech Stack

- **Frontend:** Streamlit
- **Backend:** Python
- **Database:** Supabase
- **Machine Learning:** scikit-learn
- **Face Recognition:** dlib, face recognition models
- **Voice Recognition:** Resemblyzer, librosa
- **Data Handling:** NumPy, Pandas
- **Image Processing:** Pillow
- **QR Code Generation:** Segno
- **Authentication Security:** bcrypt

## Project Structure

```text
Snapclass-Attendance/
├── app.py
├── requirements.txt
└── src/
    ├── components/
    │   ├── dialog_add_photo.py
    │   ├── dialog_attendance_results.py
    │   ├── dialog_auto_enroll.py
    │   ├── dialog_create_subject.py
    │   ├── dialog_enroll.py
    │   ├── dialog_share_subject.py
    │   ├── dialog_voice_attendance.py
    │   ├── footer.py
    │   ├── header.py
    │   └── subject_card.py
    ├── database/
    │   ├── config.py
    │   └── db.py
    ├── pipelines/
    │   ├── face_pipeline.py
    │   └── voice_pipeline.py
    ├── screens/
    │   ├── home_screen.py
    │   ├── student_screen.py
    │   └── teacher_screen.py
    └── ui/
        └── base_layout.py
```

## Installation

Clone the repository:

```bash
git clone https://github.com/harshitha-karne/Snapclass-Attendance.git
cd Snapclass-Attendance
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate the virtual environment:

For Windows:

```bash
venv\Scripts\activate
```

For macOS/Linux:

```bash
source venv/bin/activate
```

Install the required packages:

```bash
pip install -r requirements.txt
```

## Supabase Setup

This project uses Supabase for storing teachers, students, subjects, enrollments, face embeddings, voice embeddings, and attendance logs.

Create a `.streamlit/secrets.toml` file in the project root:

```toml
SUPABASE_URL = "your_supabase_project_url"
SUPABASE_KEY = "your_supabase_anon_key"
```

Required database tables:

- `teachers`
- `students`
- `subjects`
- `subject_students`
- `attendance_logs`

## Running The Project

Run the Streamlit app:

```bash
streamlit run app.py
```

The app will open locally at:

```text
http://localhost:8501
```

## How It Works

### Teacher Flow

1. Teacher registers or logs in.
2. Teacher creates a subject.
3. A subject code and QR link are generated.
4. Students join the subject using the code or link.
5. Teacher uploads classroom photos or records classroom audio.
6. AI detects students and marks attendance.
7. Teacher views attendance records.

### Student Flow

1. Student opens the Student Portal.
2. Student logs in using Face ID.
3. If the face is not recognized, the student creates a new profile.
4. Student can optionally add a voice sample.
5. Student joins subjects using subject codes.
6. Student views enrolled subjects and attendance status.

## AI Attendance Process

### Face Attendance

SnapClass detects faces from uploaded classroom images and converts them into face embeddings. These embeddings are compared with registered student face data. Recognized students are marked present automatically.

### Voice Attendance

Students can register their voice during profile creation. During attendance, the teacher records classroom audio, and SnapClass identifies matching student voices using voice embeddings.

## Requirements

Main dependencies:

```text
streamlit
numpy
pandas
scikit-learn
dlib-bin
supabase
bcrypt
segno
pillow
librosa
resemblyzer
```

If `dlib-bin` does not install correctly on Windows, install a compatible dlib wheel for your Python version.

Example:

```bash
python -m pip install dlib-19.24.1-cp311-cp311-win_amd64.whl
```

## Deployment

This project can be deployed on Streamlit Community Cloud.

Steps:

1. Push the project to GitHub.
2. Go to Streamlit Community Cloud.
3. Connect your GitHub repository.
4. Set the main file path as:

```text
app.py
```

5. Add Supabase secrets in the Streamlit Cloud secrets section.
6. Deploy the app.

## Future Improvements

- Admin dashboard
- Attendance export as CSV/PDF
- Email attendance reports
- Better duplicate enrollment handling
- Improved face recognition accuracy
- Mobile-friendly enhancements
- Class-wise attendance analytics

## Repository

GitHub Repository: [https://github.com/harshitha-karne/Snapclass-Attendance](https://github.com/harshitha-karne/Snapclass-Attendance)

## Author

**Harshitha Karne**

## License

This project is open source and available for learning, development, and academic use.