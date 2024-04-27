import socket
import os
import sys
from _thread import *
import pickle

server = ""
port = 5555
connectionCount = 0
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
player = []


try:
    s.bind((server, port))
except Exception as err:
    print("server binding failed!!!")
    print(err)

s.listen()

def connection_thread(conn, connectionCount):
    conn.send(pickle.dumps(player[connectionCount]))
    while True:
        try:
            player[connectionCount] = pickle.loads(conn.recv(4096))
            conn.sendall(pickle.dumps(player[(connectionCount+1)%2]))
        except Exception as err:
            print("error in thread function",err)
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            break
    print("connection lost")

while True:
    conn, addr = s.accept()
    print("connected to", addr)
    start_new_thread(connection_thread, (conn, connectionCount,))
    connectionCount += 1
