import pyttsx3
import requests
import speech_recognition as sr
import keyboard
import os
import subprocess as sp
import imdb
import wolframalpha
import pyautogui
import webbrowser
import time
import shutil
import psutil
from datetime import datetime
from decouple import config
from random import choice
import speedtest
from conv import random_text
import wikipedia
import pywhatkit as kit

engine = pyttsx3.init('sapi5')
engine.setProperty('volume', 1.5)
engine.setProperty('rate', 220)
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)

USER = config('USER')
HOSTNAME = config('BOT')

def speak(text):
    engine.say(text)
    engine.runAndWait()

def greet_me():
    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        speak(f"Good morning {USER}")
    elif (hour >= 12) and (hour <= 16):
        speak(f"Good afternoon {USER}")
    elif (hour >= 16) and (hour < 19):
        speak(f"Good evening {USER}")
    speak(f"I am {HOSTNAME}. How may I assist you? {USER}")

listening = False

def start_listening():
    global listening
    listening = True
    print("Started listening")

def pause_listening():
    global listening
    listening = False
    print("Stopped listening")

keyboard.add_hotkey('ctrl+alt+k', start_listening)
keyboard.add_hotkey('ctrl+alt+p', pause_listening)

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(query)
        if 'stop' not in query and 'exit' not in query:
            speak(choice(random_text))
        else:
            hour = datetime.now().hour
            if 21 <= hour < 6:
                speak("Good night sir, take care!")
            else:
                speak("Have a good day sir!")
            exit()
    except Exception:
        speak("Sorry, I couldn't understand. Can you please repeat that?")
        query = 'None'
    return query

def find_my_ip():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    return ip_address["ip"]

def search_on_wikipedia(query):
    results = wikipedia.summary(query, sentences=2)
    return results

def search_on_google(query):
    kit.search(query)

def youtube(video):
    kit.playonyt(video)

def get_news():
    news_headline = []
    result = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&category=general&apiKey=YOUR_API_KEY").json()
    articles = result["articles"]
    for article in articles:
        news_headline.append(article["title"])
    return news_headline[:6]

def weather_forecast(city):
    res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOUR_API_KEY&units=metric").json()
    weather = res["weather"][0]["main"]
    temp = res["main"]["temp"]
    feels_like = res["main"]["feels_like"]
    return weather, f"{temp}°C", f"{feels_like}°C"

def screenshot():
    img = pyautogui.screenshot()
    img.save(f"screenshot_{time.time()}.png")

def screen_recording():
    sp.run('start microsoft.windows.camera:', shell=True)
    
def put_pc_to_sleep():
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")


def internet_speed_test():
    st = speedtest.Speedtest()
    download_speed = st.download() / 10**6
    upload_speed = st.upload() / 10**6
    speak(f"Download speed is {download_speed:.2f} Mbps, Upload speed is {upload_speed:.2f} Mbps")

def find_my_ip():
    ip_address = requests.get('https://api64.ipify.org?format=json').json()
    return ip_address["ip"]

def search_on_wikipedia(query):
    results = wikipedia.summary(query, sentences=2)
    return results

def search_on_google(query):
    kit.search(query)

def youtube(video):
    kit.playonyt(video)

def get_news():
    news_headline = []
    result = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&category=general&apiKey=YOUR_API_KEY").json()
    articles = result["articles"]
    for article in articles:
        news_headline.append(article["title"])
    return news_headline[:6]

def weather_forecast(city):
    res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOUR_API_KEY&units=metric").json()
    weather = res["weather"][0]["main"]
    temp = res["main"]["temp"]
    feels_like = res["main"]["feels_like"]
    return weather, f"{temp}°C", f"{feels_like}°C"

def screenshot():
    img = pyautogui.screenshot()
    img.save(f"screenshot_{time.time()}.png")

def screen_recording():
    print("Press 'ctrl+shift+s' to start screen recording and 'ctrl+shift+q' to stop screen recording.")

    while True:
        if keyboard.is_pressed('ctrl+shift+s'):
            print("Starting screen recording")
            # Open the Xbox Game Bar
            sp.run('start shell:AppsFolder\\Microsoft.XboxGamingOverlay_8wekyb3d8bbwe!App', shell=True)
            time.sleep(2)  # Give it some time to open

            # Press Win + Alt + R to start recording
            pyautogui.hotkey('win', 'alt', 'r')
            time.sleep(2)  # Give it some time to start recording
            break

    while True:
        if keyboard.is_pressed('ctrl+shift+q'):
            print("Stopping screen recording")
            # Press Win + Alt + R to stop recording
            pyautogui.hotkey('win', 'alt', 'r')
            break
    
def put_pc_to_sleep():
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

def file_management(operation, source, destination):
    if operation == 'copy':
        shutil.copy(source, destination)
    elif operation == 'move':
        shutil.move(source, destination)
    elif operation == 'rename':
        os.rename(source, destination)
    elif operation == 'delete':
        os.remove(source)

def search_files(filename):
    for root, dirs, files in os.walk("C:\\"):
        if filename in files:
            return os.path.join(root, filename)
    return "File not found"


def internet_speed_test():
    st = speedtest.Speedtest()
    download_speed = st.download() / 10**6
    upload_speed = st.upload() / 10**6
    return download_speed, upload_speed



if __name__ == '__main__':
    greet_me()
    while True:
        if listening:
            query = take_command().lower()
            if "how are you" in query:
                speak("I am absolutely fine sir. What about you?")

            elif "open command prompt" in query:
                speak("Opening command prompt")
                os.system('start cmd')

            elif "open camera" in query:
                speak("Opening camera sir")
                sp.run('start microsoft.windows.camera:', shell=True)

            elif "open notepad" in query:
                speak("Opening Notepad for you sir")
                notepad_path = "C:\\Users\\ASUS\\AppData\\Local\\Microsoft\\WindowsApps\\notepad.exe"
                os.startfile(notepad_path)

            elif 'ip address' in query:
                ip_address = find_my_ip()
                speak(f'Your IP Address is {ip_address}.\n For your convenience, I am printing it on the screen sir.')
                print(f'Your IP Address is {ip_address}')

            elif "open youtube" in query:
                speak("What do you want to play on YouTube sir?")
                video = take_command().lower()
                youtube(video)

            elif "open google" in query:
                speak(f"What do you want to search on Google {USER}?")
                search_query = take_command().lower()
                search_on_google(search_query)

            elif "wikipedia" in query:
                speak("What do you want to search on Wikipedia sir?")
                search = take_command().lower()
                results = search_on_wikipedia(search)
                speak(f"According to Wikipedia, {results}")
                speak("I am printing it on the terminal")
                print(results)

            elif "give me news" in query:
                speak(f"I am reading out the latest headlines of today, sir")
                speak(get_news())
                speak("I am printing it on the screen sir")
                print(*get_news(), sep='\n')

            elif 'weather' in query:
                ip_address = find_my_ip()
                speak("Tell me the name of your city")
                city = input("Enter the name of your city: ")
                speak(f"Getting weather report for your city {city}")
                weather, temp, feels_like = weather_forecast(city)
                speak(f"The current temperature is {temp}, but it feels like {feels_like}")
                speak(f"Also, the weather report talks about {weather}")
                speak("For your convenience, I am printing it on the screen sir.")
                print(f"Description: {weather}\nTemperature: {temp}\nFeels like: {feels_like}")

            elif "take a screenshot" in query:
                screenshot()
                speak("Screenshot taken")

            elif "start screen recording" in query:
                screen_recording()
                speak("Starting screen recording")

            elif "search file" in query:
                speak("What is the name of the file you are looking for?")
                filename = take_command().lower()
                filepath = search_files(filename)
                speak(filepath)
                print(filepath)

            elif "sleep" in query:
                put_pc_to_sleep()
                speak("Putting the PC to sleep")

            elif "file operation" in query:
                speak("What operation do you want to perform? (copy, move, rename, delete)")
                operation = take_command().lower()
                speak("Please provide the source path")
                source = input("Source path: ")
                speak("Please provide the destination path")
                destination = input("Destination path: ")
                file_management(operation, source, destination)

            elif "internet speed test" in query:
                internet_speed_test()
