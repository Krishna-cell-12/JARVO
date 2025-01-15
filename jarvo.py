#JARVO.py

import pyttsx3
import speech_recognition as sr

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print("Say that again please...")
        return "none"
    return query

if __name__ == "__main__":
    speed = engine.getProperty('rate')
    engine.setProperty('rate', 150)
    speak("  ")
    while True:
        query = takeCommand().lower()
        if 'exit' in query:
            speak("Goodbye!")
            break
        elif 'hello' in query:
            speak("Hello! How can I help you today?")
        else:
            speak("I'm sorry, I didn't understand your request.")

    
