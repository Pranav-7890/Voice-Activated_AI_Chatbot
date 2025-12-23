# Voice-Activated AI Chatbot

A Python-based voice assistant that uses NLP and Speech Recognition to perform tasks.

## Features
- **Voice Recognition**: Uses Google Speech API.
- **Wikipedia Integration**: Fetches summaries of any topic.
- **System Commands**: Can open apps (Notepad), lock the PC, and tell the time.
- **Automation**: Can take voice notes and save them to a file.

## Setup Instructions
1. Install Python 3.8+
2. Install `uv` package manager.
3. Run `uv sync` to install dependencies.
4. Run the bot: `python main.py`

## Dependencies
- speechrecognition
- pyttsx3
- wikipedia
- PyAudio
- "pyaudio>=0.2.14"
- "pyttsx3>=2.99"
- "setuptools>=80.9.0"
- "speechrecognition>=3.14.4"
- "wikipedia>=1.4.0"
- "wikipedia-api>=0.8.1"