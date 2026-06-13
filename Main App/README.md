<div align="center">

# 📸 Attendance by Selfie — CNN

**Making Attendance Faster Using AI**

SnapClass is an intelligent attendance management system that leverages facial recognition technology to streamline the attendance process. Built with Python and Streamlit, it provides a seamless experience for both teachers and students.

[![Python](https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white)](https://www.python.org/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit&logoColor=white)](https://streamlit.io/)
[![Supabase](https://img.shields.io/badge/Supabase-Database-3ECF8E?logo=supabase&logoColor=white)](https://supabase.com/)
[![License](https://img.shields.io/badge/License-MIT-green)](https://opensource.org/licenses/MIT)
[![Open Source](https://img.shields.io/badge/Open-Source-yellow)](https://github.com/Tanvir-Sheikh-R/Attendance-by-selfie---CNN)

🌐 [Live Demo](https://landing-page-for-attendance-by-self.vercel.app) &nbsp;|&nbsp; 🐛 [Report Bug](https://github.com/Tanvir-Sheikh-R/Attendance-by-selfie---CNN/issues) &nbsp;|&nbsp; ✨ [Request Feature](https://github.com/Tanvir-Sheikh-R/Attendance-by-selfie---CNN/issues)

</div>

---

## 🎯 Features

<div align="center">

| Feature | Description |
|:---|:---|
| 📷 **AI Facial Recognition** | Automatically recognize and verify student identities |
| 👥 **Dual Interface** | Separate dashboards for teachers and students |
| 🔳 **QR Code Generation** | Generate QR codes for quick attendance verification |
| 🔐 **Secure Authentication** | Login system with bcrypt password encryption |
| 🎙️ **Audio Analysis** | Voice/audio recognition for enhanced verification |
| ☁️ **Cloud Database** | Supabase-powered cloud storage and data management |
| 🌐 **Multi-Platform** | Streamlit-based web app, accessible anywhere |
| ⚡ **No GPU Required** | Runs entirely on CPU |

</div>

---

## 🛠️ Tech Stack

<div align="center">

| Layer | Technology |
|:---:|:---:|
| Frontend | Streamlit |
| Face Detection & Encoding | dlib-bin, face_recognition_models |
| Face Classification | scikit-learn (SVM / KNN classifier) |
| Voice Recognition | Resemblyzer, Librosa, webrtcvad-wheels |
| Database | Supabase (PostgreSQL via PostgREST) |
| Password Security | Bcrypt |
| QR Code | Segno |
| Image Processing | Pillow, NumPy |
| Data Handling | Pandas |
| Package Bridging | setuptools |

</div>

---

## 📋 Prerequisites

Before installing, make sure you have the following:

- **Python 3.10** (recommended; dlib-bin has strict version requirements)
- **pip** package manager
- **Git** installed and configured
- A **Supabase** account with a project created
- **CMake** and a **C++ compiler** if building dlib from source (not needed if using `dlib-bin`)
- Microphone and webcam access on your machine

---

## ⚙️ Installation

**1. Clone the repository**

```bash
git clone https://github.com/Tanvir-Sheikh-R/Attendance-by-selfie---CNN.git
cd Attendance-by-selfie---CNN
```

**2. Create and activate a virtual environment**

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS / Linux
python -m venv venv
source venv/bin/activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Set up environment variables**

Create a `.env` file in the root directory:
"if you use Supabase as your database"

```env
SUPABASE_URL=your_supabase_project_url
SUPABASE_KEY=your_supabase_anon_key
```

> ⚠️ Never commit your `.env` file. It is already listed in `.gitignore`.

**5. Set up Supabase tables**

In your Supabase SQL editor, create the required tables for students, attendance records, and credentials. Refer to the schema in `docs/schema.sql` if provided, or set up tables matching the field names used in `src/`.

---

## ▶️ Running the Application

```bash
streamlit run app.py
```

The app will open in your browser at `http://localhost:8501`.

**First time setup:**

1. Register students through the admin panel — capture face samples and record a short voice clip
2. The system trains the face classifier and stores voice embeddings
3. Students can then mark attendance by taking a selfie and speaking a passphrase

---

## 📁 Project Structure

```
Attendance-by-selfie---CNN/
│
├── app.py                    # Main Streamlit entry point
│
├── src/
│   ├── face_recognition/     # Face encoding, classifier training & prediction
│   ├── voice_recognition/    # Voice embedding pipeline using Resemblyzer
│   ├── database/             # Supabase query functions
│   ├── auth/                 # Login, registration, Bcrypt password handling
│   └── utils/                # QR code generation, image helpers
│
├── .streamlit/
│   └── config.toml           # Streamlit theme and server config
│
├── .devcontainer/            # Dev container configuration
│
├── Landing Page/             # Static HTML/CSS landing page assets
│
├── patch_resemblyzer.py      # Compatibility patch for Resemblyzer on deployment
│
├── requirements.txt          # Python dependencies
├── packages.txt              # System-level packages (for Streamlit Cloud)
├── .gitignore
└── README.md
```

---

## 🖥️ Usage

### For Students
1. Open the app in your browser
2. Select **Mark Attendance**
3. Allow camera and microphone access
4. Take a selfie — the system detects and identifies your face
5. Speak the passphrase for voice verification
6. Attendance is confirmed and saved automatically

### For Teachers
1. Log in with admin credentials
2. **Register Student** — Add name, ID, capture face images, record voice sample
3. **View Attendance** — Browse daily attendance logs with filters
4. **Manage Students** — Edit or remove student profiles
5. **Export Records** — Download attendance as CSV via Pandas

---

## 🔐 Security Factors

<div align="center">

| Factor | Details |
|:---:|:---|
| 🔑 **Password Encryption** | All passwords hashed with `bcrypt`; plaintext never stored |
| 🌿 **Environment Variables** | Supabase credentials stored in `.env`, excluded via `.gitignore` |
| 🧬 **No Raw Biometric Storage** | Faces stored as 128-dim vectors; voice as embeddings, not audio |
| 🛡️ **Supabase RLS** | Row-Level Security policies scope access per role |
| 🔒 **Session Management** | Streamlit session state prevents unauthorized page access |
| ✅ **Input Validation** | All form inputs validated before any database query |

</div>

---

## 🤝 Contribution

Contributions are welcome! To contribute:

1. Fork the repository
2. Create a new branch for your feature

```bash
git checkout -b feature/your-feature-name
```

3. Make your changes and commit with a clear message

```bash
git commit -m "Add: your feature description"
```

4. Push to your fork and open a Pull Request

```bash
git push origin feature/your-feature-name
```

Please make sure your code follows the existing structure and doesn't break any existing functionality before opening a PR.

---

## 📄 License

This project is licensed under the **MIT License**.

You are free to use, modify, and distribute this project for personal or commercial purposes, provided that the original license and copyright notice are included.

---

<div align="center">
  Made with ❤️ by <a href="https://github.com/Tanvir-Sheikh-R">Tanvir Sheikh</a>
</div>
