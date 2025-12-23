import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import time

# Function to initialize the engine inside speak to prevent "silent" voice bugs
def speak(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)
    engine.setProperty('rate', 170) # Slows down the speed slightly for clarity
    print(f"AI: {audio}")
    engine.say(audio)
    engine.runAndWait()
    # This helps release the audio resource
    engine.stop()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Good Morning!")
    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")
    speak("I am ready. How can I help you?")

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.8 # Slightly faster response
        r.adjust_for_ambient_noise(source, duration=1) # Cleans up background noise
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")
    except sr.UnknownValueError:
        print("I didn't catch that. Could you repeat?")
        return "None"
    except sr.RequestError:
        speak("I'm sorry, my speech service is down. Please check your internet connection.")
        return "None"
    except Exception:
        return "None"
    return query.lower()
    

if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand()

        # specific keyword matching
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            # This line removes "search", "for", and "wikipedia" to get the clean keyword
            search_query = query.replace("wikipedia", "").replace("search", "").replace("for", "").strip()
            try:
                results = wikipedia.summary(search_query, sentences=2)
                speak(f"According to Wikipedia, {results}")
            except Exception:
                speak("I couldn't find a specific page for that. Could you be more specific?")

        elif 'open google' in query:
            speak("Opening Google")
            webbrowser.open("google.com")

        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%I:%M %p") # 12-hour format is friendlier
            speak(f"The time is {strTime}")

        elif 'shutdown' in query:
            speak("Shutting down the system in 10 seconds. Make sure you save your work.")
            # os.system("shutdown /s /t 10") # Uncomment this to actually shutdown
            break

        # COMMAND: Take a Note
        elif 'write a note' in query or 'make a note' in query:
            speak("What should I write, sir?")
            note = takeCommand()
            if note != "None":
                with open("mynotes.txt", "a") as f:
                    # This adds a timestamp so you know when you wrote it
                    f.write(f"{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}: {note}\n")
                speak("I've saved that to your notes file.")

        # COMMAND: Open Notepad
        elif 'open notepad' in query:
            speak("Opening Notepad for you.")
            os.system("notepad.exe")

        # COMMAND: Lock the PC
        elif 'lock my computer' in query:
            speak("Locking the device.")
            import ctypes
            ctypes.windll.user32.LockWorkStation()

        # COMMAND: Search Google directly
        elif 'google search' in query:
            speak("What should I search for on Google?")
            search_data = takeCommand()
            if search_data != "None":
                webbrowser.open(f"https://www.google.com/search?q={search_data}")
                speak(f"Here is what I found for {search_data}")

        elif 'exit' in query or 'stop' in query:
            speak("Goodbye! Have a nice day.")
            break