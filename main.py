import speech_recognition as sr
import pyttsx3
import os
import webbrowser
from datetime import datetime
from googleapi_testing import client

engine = pyttsx3.init()

def say(txt):
    engine.say(txt)
    print(f"J.A.R.V.I.S: {txt}")
    engine.runAndWait()

def takeCommand():
    # r = sr.Recognizer()
    # with sr.Microphone() as source:
    #     r.pause_threshold = 0.6
    #     print('Listening...')
    #     audio = r.listen(source)
    #
    # try:
    #     print('recognizing...')
    #     query = r.recognize_google(audio, language = 'en-in')
    #     print(f"User: {query}")
    #     return query
    # except Exception as e:
    #     return 'There\'s some error.'
    return input('Enter command: ')

def opensites(site):
    webbrowser.open(site)

def smart_response(prompt):
    return f"Respond as concisely and as intelligently as your are the Jarvis from Iron Man movies to the following prompt. Limit response to minimum necessary lines possible. No markdown formatting or asterisks. Prompt: {prompt}"

if __name__ == '__main__':
    say('Hello')
    while 1:
        text = takeCommand()

        sites = [['youtube', 'https://youtube.com'], ['Google', 'https://google.com'], ['wikipedia', 'https://wikipedia.com'], ['instagram', 'https://www.instagram.com']]

        # for site in sites:
        #     if f'open {site[0]}'.lower() in text .lower():
        #             say(f'opening {site[0]}')
        #             opensites(site[1])

        if 'open'.lower() in text.lower():
            for site in sites:
                if f'{site[0]}'.lower() in text.lower():
                    say(f'Opening {site[1]}')
                    opensites(site[1])

        elif 'play'.lower() in text.lower():
            if 'music'.lower() in text.lower():
                say('Sure, why not? Here\'s some music for you.')
                os.startfile(r"C:\Users\ABBAS\Downloads\Warriyo, LXNGVX - Mortals Funk Remix [NCS Release].mp3")

        elif 'the time'.lower() in text.lower():
            now = datetime.now()
            time = now.strftime("%I:%M %p")
            say(f"time is {time}")

        elif 'open discord'.lower() in text.lower():
            say('opening discord')
            os.startfile(r"C:\Users\ABBAS\AppData\Local\Discord\app-1.0.9192\Discord.exe")

        elif ('quit'.lower() or 'exit'.lower() or 'shut'.lower()) in text.lower():
            say('Sure Sir, see you later.')
            exit()
        else:
            response = client.models.generate_content(model = "gemini-2.0-flash", contents = smart_response(text))
            say(response.text.replace('*', ''))