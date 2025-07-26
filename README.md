# 🤖 Friday – Your Linux-Based Personal Voice Assistant

Friday is a voice-activated personal assistant built in Python for Linux. It understands your speech, parses intent, executes tasks like opening apps, and speaks back responses — all offline and fully customizable.<br>

---

## 🚀 Features<br>

- 🎙️ Voice Recognition (Google Speech API or Whisper)<br>
- 🗣️ Text-to-Speech (Offline via pyttsx3)<br>
- ⚙️ Intent Detection via Rules (Expandable to AI-based NLP)<br>
- 🧠 Task Execution (Open VS Code, shutdown system, etc.)<br>
- 📦 Modular architecture (easy to extend)<br>
- 🔌 Runs entirely offline (optional GPT integration)<br>

---

## 🛠️ Requirements<br>

Make sure Python 3.10+ is installed. You also need:<br>

```bash
sudo apt update
sudo apt install portaudio19-dev python3-pyaudio python3-dev
pip install -r requirements.txt
```
Requirements.txt<br>
```bash
SpeechRecognition
pyttsx3
pyaudio
```

📁 Project Structure<br>

friday/<br>
├── main.py                  # Entry point<br>
├── modules/<br>
│   ├── speech_input.py      # Speech to Text<br>
│   ├── speech_output.py     # Text to Speech<br>
│   ├── intent_handler.py    # Intent parser<br>
│   └── task_executor.py     # Executes system-level tasks<br>


▶️ How to Run Friday<br>

```bash
cd friday
python3 main.py
```

👨‍💻 Maintainer<br>
Gaurav Sharma<br>
AI/ML Enthusiast | Python | Networks<br>
