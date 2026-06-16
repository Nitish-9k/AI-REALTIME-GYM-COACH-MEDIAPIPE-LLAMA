# 🏋️‍♀️ AI Real-time Gym Coach

An AI-powered real-time fitness coaching web app built with **Streamlit**, **MediaPipe**, and **LLaMA (via Groq)**. It uses your webcam to analyze exercise form, count reps and sets, and deliver live voice feedback — like having a personal trainer in your browser.

🚀 **Live App:** [ai-powered-real-time-gym-trainer.streamlit.app](https://ai-powered-real-time-gym-trainer.streamlit.app/)

---

## ✨ Features

- **Real-time Pose Detection** — MediaPipe tracks 33 body landmarks via your webcam to analyze movement frame by frame.
- **Exercise Rep & Set Counting** — Automatically counts reps and tracks set completion against your plan.
- **Form & Biomechanics Feedback** — Measures joint angles, body alignment, depth, and stability per exercise and flags deviations.
- **AI Voice Coaching** — LLaMA (via Groq API) generates contextual coaching cues; gTTS converts them to speech that autoplays in the browser.
- **5 Supported Exercises:**
  - Squats *(knee angle, back angle, hip depth)*
  - Push-ups *(elbow angle, body alignment, hip position)*
  - Lunges *(front knee angle, torso angle, balance)*
  - Bicep Curls / Dumbbell *(elbow angle, shoulder stability, swing detection)*
  - Shoulder Press *(elbow angle, arm extension, back arch detection)*
- **Workout Planning** — Set your exercise, target sets, and reps before each session from the sidebar.
- **Workout History** — Sessions are persisted to a local SQLite database and displayed as an aggregated history table.
- **User Authentication** — Login wall to keep sessions user-specific.

---

## 🧱 Tech Stack

| Layer | Technology |
|---|---|
| Frontend / UI | Streamlit |
| Pose Estimation | MediaPipe Pose |
| Video Streaming | streamlit-webrtc + OpenCV |
| LLM Coach | LLaMA 3 via Groq API |
| Text-to-Speech | gTTS (Google Text-to-Speech) |
| Data | SQLite (via custom repository) + Pandas |
| Styling | Custom CSS + local fonts |

---

## 📁 Project Structure

```
├── main.py                   # Streamlit app entry point
├── requirements.txt
├── packages.txt
├── core/                     # Core logic (rep counting, angle math)
├── detectors/                # Per-exercise pose detectors
├── ml_models/                # ML model assets
├── services/
│   ├── auth/                 # Login wall
│   ├── coaching/             # LLM coach, TTS, voice pipeline
│   ├── config/               # Exercise options config
│   ├── persistence/          # SQLite DB repository
│   ├── state/                # Streamlit session state defaults
│   ├── tracking/             # Metrics sync
│   ├── ui/                   # CSS loader, font injector
│   └── vision/               # WebRTC video processor
├── static/                   # CSS and font files
└── .devcontainer/            # Dev container config
```

---

## ⚙️ Setup & Installation

### Prerequisites

- Python 3.10+
- A [Groq API key](https://console.groq.com/) (free tier available)
- Webcam

### 1. Clone the repo

```bash
git clone https://github.com/Nitish-9k/AI-REALTIME-GYM-COACH-MEDIAPIPE-LLAMA.git
cd AI-REALTIME-GYM-COACH-MEDIAPIPE-LLAMA
```

### 2. Install system dependencies

```bash
# On Ubuntu/Debian (required for OpenCV headless + WebRTC)
cat packages.txt | xargs sudo apt-get install -y
```

### 3. Install Python dependencies

```bash
pip install -r requirements.txt
```

### 4. Set your Groq API key

Create a `.env` file in the project root:

```env
GROQ_API_KEY=your_groq_api_key_here
```

Or, if deploying to Streamlit Cloud, add it under **Settings → Secrets**:

```toml
GROQ_API_KEY = "your_groq_api_key_here"
```

### 5. Run the app

```bash
streamlit run main.py
```

---

## 🖥️ How to Use

1. Open the app and log in.
2. In the **sidebar**, select an exercise, set your target sets and reps, and click **Start Workout**.
3. Allow camera access in your browser when prompted.
4. Perform your exercise in front of the webcam — the AI will count your reps and call out coaching feedback via voice.
5. Real-time metrics (joint angles, form status) are shown live in the sidebar.
6. Click **End Workout** when done. Your session is saved to history.

---

## 🌐 Deploying to Streamlit Cloud

1. Push your repo to GitHub.
2. Go to [share.streamlit.io](https://share.streamlit.io) and connect your repo.
3. Set `main.py` as the entry point.
4. Add `GROQ_API_KEY` under **App Settings → Secrets**.
5. Deploy — Streamlit Cloud will install packages from both `packages.txt` and `requirements.txt` automatically.

---

## 📦 Dependencies

```
streamlit==1.54.0
streamlit-webrtc==0.64.5
mediapipe==0.10.14
opencv-contrib-python-headless==4.10.0.84
pandas==2.2.3
groq>=0.12.0
gtts==2.5.3
python-dotenv==1.2.2
```

---

## 🤝 Contributing

Pull requests are welcome! For major changes, please open an issue first to discuss what you'd like to change.


---

> Built with 💪 by [Nitish-9k](https://github.com/Nitish-9k)
