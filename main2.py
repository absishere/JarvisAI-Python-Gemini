import speech_recognition as sr
import pyttsx3
import os
import webbrowser
from datetime import datetime
from google import genai
from googleapi_testing import client

engine = pyttsx3.init()

def say(txt):
    engine.say(txt)
    print(f"J.A.R.V.I.S: {txt}")
    engine.runAndWait()

def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        r.pause_threshold = 0.6
        print('Listening...')
        audio = r.listen(source)

    try:
        print('recognizing...')
        query = r.recognize_google(audio, language = '')
        print(f"User: {query}")
        return query
    except Exception as e:
        return 'There\'s some error.'

if __name__ == '__main__':
    say('Hello')
    while 1:
        text = takeCommand()
        response = client.models.generate_content(model = "gemini-1.5-flash-latest", contents = text)
        say(response.text.strip('*'))