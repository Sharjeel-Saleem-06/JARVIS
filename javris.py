import pyttsx3
import requests
import speech_recognition as sr
import keyboard
import os
import subprocess as sp
# import imdb
# import wolframalpha
import pyautogui
import webbrowser
import time

from datetime import datetime
from decouple import config
from random import choice
from conv import random_text
from online import get_ip_address ,search_on_google, search_on_wikipedia, youtube
# from online import find_my_ip, search_on_google, search_on_wikipedia, youtube, send_email, get_news, weather_forecast

# Initialize the text-to-speech engine
engine = pyttsx3.init('sapi5')
engine.setProperty('volume', 1.5)
engine.setProperty('rate', 230)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

# For username and bot name from config file using decouple
USER = config('USER')
HOSTNAME = config('BOT')

# Function to recognize speech
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function for greeting user according to its time
def greet_me():
    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        speak(f"Good morning {USER}")
    elif (hour >= 12) and (hour <= 16):
        speak(f"Good afternoon {USER}")
    elif (hour >= 16) and (hour < 19):
        speak(f"Good evening {USER}")
    speak(f"I am {HOSTNAME}. How may i assist you? {USER}")

# Control listening state
listening = False

def start_listening():
    global listening
    listening = True
    print("started listening ")

def pause_listening():
    global listening
    listening = False
    print("stopped listening")


keyboard.add_hotkey('ctrl+alt+k', start_listening)
keyboard.add_hotkey('ctrl+alt+p', pause_listening)


# Initialize microphone and speech recognizer
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing....")
        queri = r.recognize_google(audio, language='en-in')
        print(queri)
        if not 'stop' in queri or 'exit' in queri:
            speak("")
        else:
            hour = datetime.now().hour
            if hour >= 21 and hour < 6:
                speak("Good night sir,take care!")
            else:
                speak("Have a good day sir!")
            exit()

    except Exception:
        speak("Sorry I couldn't understand. Can you please repeat that?")
        queri = 'None'
    return queri

# Main calling
if __name__ == '__main__':
    greet_me()
    while True:
        if listening:
            query = take_command().lower()
            if "how are you" in query:
                speak("I am absolutely fine sir. What about you")
            elif "what is pubg" in query:
                speak("Pubg is a game of stupid people")

            elif "open command prompt" in query:
                speak("Opening Command PRompt")
                os.system("start cmd")

            elif "open camera" in query:
                speak("Opening camera")   
                sp.run('start microsoft.windows.camera:',shell=True) 

            elif "open notepad" in query:
                speak("opening notepad for you sir")
                notepad_path="C:\\Windows\\notepad.exe"
                os.startfile(notepad_path)    

            elif "tell me ip address" in query:
                ip=get_ip_address()
                speak(f"your ip address is{ip}")
                
            elif "youtube"in query:
                speak("sharry what do you want to play")
                video=take_command().lower()
                youtube(video)

            elif "open wikipedia"in query:
                speak("What do you want to search")
                query=take_command().lower()
                search_on_wikipedia(query)   
                speak("According to wikipedia,{results}")

            elif "open google"in query:
                speak("sharry What do you want to search")
                query=take_command().lower()
                search_on_google(query)   
