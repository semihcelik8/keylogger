import socket
import threading

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("127.0.0.1", 62121))

def process_input():
    while True:
        input_data = input(">> ")
        if input_data == "monitor":
            try:
                conn.send("monitor".encode("utf-8"))
                print("Sent monitor command")
                text_file_data = (conn.recv(1048576)).decode("utf-8")
                print(text_file_data)
            except:
                print("[FAILED] Could not send " + str(input_data) + " command")
        elif input_data == "refresh":
            try:
                conn.send("refresh".encode("utf-8"))
                response = (conn.recv(1024)).decode("utf-8")
                print(response)
            except:
                print("[FAILED] Could not send " + str(input_data) + " command")

threading.Thread(target = process_input).start()

while True:
    s.listen()
    conn, addr = s.accept()
    print(str(addr) + " joined")
