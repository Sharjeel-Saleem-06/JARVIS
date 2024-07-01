import requests
import wikipedia
# toacess gogle yt, have predefined function in librarty
import pywhatkit 
import socket




def get_ip_address():
    hostname = socket.gethostname()
    ip_address = socket.gethostbyname(hostname)
    return ip_address

# Usage
ip = get_ip_address()
print(f"IP Address of the computer: {ip}")
