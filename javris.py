import socket
import pyttsx3  # Text-to-speech conversion library
import requests  # Library to make HTTP requests
import speech_recognition as sr  # Library for performing speech recognition
import keyboard  # Module for detecting keyboard events
import os  # Provides functions for interacting with the operating system
import subprocess as sp  # Subprocess management module
import imdb  # IMDB API client library
import wolframalpha  # WolframAlpha API client library
import pyautogui  # Library to control the mouse and keyboard
import webbrowser  # Library to open URLs in the browser
import time  # Time-related functions
import psutil  # System and process utilities
from datetime import datetime  # Date and time functions
from decouple import config  # Library to read configuration from .env file
from random import choice  # Library for generating random selections
import speedtest  # Library to test internet speed
import pywhatkit as kit  # Library to send WhatsApp messages and perform various operations

# Initialize the text-to-speech engine
engine = pyttsx3.init('sapi5')
engine.setProperty('volume', 1.5)  # Set the volume
engine.setProperty('rate', 220)  # Set the speech rate
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Set the voice

# Read user and bot name from .env file
USER = config('USER')
HOSTNAME = config('BOT')
random_text='ok'

# Function to convert text to speech and play it
def speak(text):
    engine.say(text)
    engine.runAndWait()

# Function to greet the user based on the time of day
def greet_me():
    hour = datetime.now().hour
    if (hour >= 6) and (hour < 12):
        speak(f"Good morning {USER}")
    elif (hour >= 12) and (hour <= 16):
        speak(f"Good afternoon {USER}")
    elif (hour >= 16) and (hour < 19):
        speak(f"Good evening {USER}")
    speak(f"I am {HOSTNAME}. How may I assist you? {USER}")

# Variable to track if the application is listening
listening = False

# Function to start listening for commands
def start_listening():
    global listening
    listening = True
    print("Started listening")

# Function to stop listening for commands
def pause_listening():
    global listening
    listening = False
    print("Stopped listening")

# Assign hotkeys to start and stop listening
keyboard.add_hotkey('ctrl+alt+k', start_listening)
keyboard.add_hotkey('ctrl+alt+p', pause_listening)

# Function to take a voice command from the user
def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1  # Adjusts the pause threshold for speech recognition
        audio = r.listen(source)  # Listens for the user's input

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')  # Recognizes the speech using Google API
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

# Function to find the user's IP address
def find_my_ip():
    try:
        # Use the socket library to get the IP address
        hostname = socket.gethostname()
        ip_address = socket.gethostbyname(hostname)
    except Exception as e:
        ip_address = "Unable to get IP Address"
        print(f"Error: {e}")
    
    return ip_address

# Function to search for a query on Wikipedia
def search_on_wikipedia(query):
    results = wikipedia.summary(query, sentences=2)
    return results

# Function to search for a query on Google
def search_on_google(query):
    kit.search(query)

# Function to play a YouTube video
def youtube(video):
    kit.playonyt(video)

# Function to get the latest news headlines
def get_news():
    news_headline = []
    result = requests.get(f"https://newsapi.org/v2/top-headlines?country=in&category=general&apiKey=YOUR_API_KEY").json()
    articles = result["articles"]
    for article in articles:
        news_headline.append(article["title"])
    return news_headline[:6]

# Function to get the weather forecast for a city
def weather_forecast(city):
    res = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid=YOUR_API_KEY&units=metric").json()
    weather = res["weather"][0]["main"]
    temp = res["main"]["temp"]
    feels_like = res["main"]["feels_like"]
    return weather, f"{temp}°C", f"{feels_like}°C"

# Function to take a screenshot
def screenshot():
    img = pyautogui.screenshot()
    img.save(f"screenshot_{time.time()}.png")

# Function to start screen recording using Xbox Game Bar
def screen_recording():
    print("Press 'ctrl+shift+s' to start screen recording and 'ctrl+shift+q' to stop screen recording.")

    while True:
        if keyboard.is_pressed('ctrl+shift+s'):
            print("Starting screen recording")
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

# Function to put the PC to sleep
def put_pc_to_sleep():
    os.system("rundll32.exe powrprof.dll,SetSuspendState 0,1,0")

# Function to manage files (copy, move, rename, delete)
def file_management(operation, source, destination):
    if operation == 'copy':
        shutil.copy(source, destination)
    elif operation == 'move':
        shutil.move(source, destination)
    elif operation == 'rename':
        os.rename(source, destination)
    elif operation == 'delete':
        os.remove(source)

# Function to search for a file in the system
def search_files(filename):
    for root, dirs, files in os.walk("C:\\"):
        if filename in files:
            return os.path.join(root, filename)
    return "File not found"

# Function to test internet speed
def internet_speed_test():
    st = speedtest.Speedtest()
    download_speed = st.download() / 10**6
    upload_speed = st.upload() / 10**6
    return download_speed, upload_speed

# Main function to start the assistant
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


            elif "internet speed test" in query:
                internet_speed_test()
