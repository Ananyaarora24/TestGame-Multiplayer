import socket
from _thread import *


server = "localhost"
port = 5555

a = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    a.bind((server,port))
except socket.error as n:
    str(n)

a.listen(2)
print("Waiting for a connection, Server Started")

def read_position(data_str): #string to tuple
    data_str = data_str.split(",")
    return int(data_str[0]),int(data_str[1])

def make_position(data_tup):#tuple to string
    return str(data_tup[0])+","+str(data_tup[1])

position =[(0,0),(100,100)]

def threaded_client(conn, player):
    conn.send(str.encode(make_position(position[player])))
    reply = ""
    while True:
        try:
            data = read_position(conn.recv(2043).decode())
            position[player] = data

            if not data:
                print("Disconnected")
                break
            else:
                if player == 1:
                    reply = position[0]
                else:
                    reply = position[1]
                print("Recieved: ", data)
                print("Sending: ", reply)
            conn.sendall(str.encode(make_position(reply)))
        except:
            break
    print("Lost connection")
    conn.close()

currP = 0
while True:
    conn, addr = a.accept()
    print("Connected to:", addr)

    start_new_thread(threaded_client, (conn, currP))
    currP +=1
