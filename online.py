import requests
import wikipedia
# toacess gogle yt, have predefined function in librarty
import pywhatkit 
import socket
import pywhatkit as kit




def get_ip_address():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address


def search_on_wikipedia(query):
    result=wikipedia.summary(query, sentences=2)
    return result


def search_on_google(query):
    kit.search(query)

def youtube(video):
    kit.playonyt(video)    