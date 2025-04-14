# 🧑‍🏫 Face Recognition Attendance System

An AI-powered 2-factor Attendance web application for managing student attendance using face recognition. It allows teachers to automate attendance tracking, manage subject-wise data, and export attendance to Excel with support for both facial and manual entry.

---

## 🚀 Features

- ✅ Face recognition using webcam
- ✅ Student registration with face encoding
- ✅ Subject-wise and date-wise attendance tracking
- ✅ Manual attendance marking (checkboxes)
- ✅ Excel export for attendance reports
- ✅ Filtering students based on present in collage for better approach
- ✅ 2- Factor authentication to mange proxy entries


---

## 🏗️ Project Structure

```
face-recognition-attendance/
├── static/                      # CSS, JS files
├── templates/                  # HTML templates (admin_login, register, attendance, etc.)
├── uploads/                    # Registered user images
├── app.py                      # Main Flask application
├── EncodeGenerator.py          # Script for encoding faces
├── requirements.txt            # Python dependencies
└── README.md                   # This file
```

---

## 🧰 Technologies Used

- **Python 3.12.5**
- **Flask 3.0.3**
- **OpenCV**
- **face_recognition**
- **SQLite3**
- **HTML/CSS/JavaScript**
- **Pandas / openpyxl** (for Excel export)

---

## ⚙️ Setup Instructions

### 🔧 Prerequisites

- Python 3.x
- Webcam
- pip

### 🛠️ Installation

```bash
git clone https://github.com/yourusername/face-recognition-attendance.git
cd face-recognition-attendance
pip install -r requirements.txt
```

### 🏃 Run the Project

```bash
python app.py
```

Open in browser: [http://127.0.0.1:5000](http://127.0.0.1:5000)

---

## 🗂️ Key Routes / Endpoints

| Method | Route                  | Description |
|--------|------------------------|-------------|
| GET    | `/`                    | Home dashboard |
| GET/POST | `/admin_login`       | Admin login page |
| GET/POST | `/register`          | Register new student with image |
| POST   | `/check_face`          | Capture face from webcam & mark attendance |
| POST   | `/attendance`          | Mark/view attendance for a subject |
| POST   | `/modify_admin`        | Modify admin credentials |
| GET/POST | `/download_attendance` | Export attendance for subject/date range |
| POST   | `/delete_entry/<id>`   | Delete a student from DB and encodings |

---

## 📦 Deployment

You can deploy this Flask app on:

- 🔹 [Render](https://render.com/)
- 🔹 [Railway](https://railway.app/)
- 🔹 Your own VPS with Gunicorn + Nginx
- 🔹 [Heroku (legacy)](https://devcenter.heroku.com/articles/getting-started-with-python)

---

## 🙋‍♂️ Author

**Sayantan Mitra**

- GitHub: [@sayantanmitra](https://github.com/SayantanMitra2004)
- Built as a college project (2025)

---


## 🙏 Acknowledgements

- [face_recognition by @ageitgey](https://github.com/ageitgey/face_recognition)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [OpenCV](https://opencv.org/)
