# 🤖Voice-Activated AI Chatbot

A Python-based voice assistant that uses NLP and Speech Recognition to perform tasks.

## Features

- **Voice Recognition:** Uses Google Speech API to understand user voice commands.
- **Wikipedia Integration:** Fetches concise summaries for any searched topic.
- **System Commands:** Opens applications like Notepad, locks the PC, and tells the current time.
- **Automation:** Takes voice notes and saves them with timestamps in a text file.


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

## Requirements
- "pyaudio>=0.2.14"
- "pyttsx3>=2.99"
- "setuptools>=80.9.0"
- "speechrecognition>=3.14.4"
- "wikipedia>=1.4.0"

- "wikipedia-api>=0.8.1"
