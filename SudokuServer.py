import copy
import socket
import os
import sys
from _thread import *
import pickle
from GameMode import OnlineGameMode
import sudokuGen

server = ""
port = 5555
connectionCount = 0
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
player_map:dict[int, list[OnlineGameMode,OnlineGameMode]] = {}
game_id = 0
player_id = -1


try:
    s.bind((server, port))
except Exception as err:
    print("server binding failed!!!")
    print(err)

s.listen()

def connection_thread(conn, connectionCount, game_id , player_id):
    conn.send(pickle.dumps(player_map[game_id][player_id]))
    while True:
        try:
            flag = sudokuGen.checkGameStatus(player_map[game_id][player_id].grid)
            # player[connectionCount] = pickle.loads(conn.recv(4096))
            conn.sendall(pickle.dumps(player_map[(connectionCount+1)%2]))
        except Exception as err:
            print("error in thread function",err)
            exc_type, exc_obj, exc_tb = sys.exc_info()
            fname = os.path.split(exc_tb.tb_frame.f_code.co_filename)[1]
            print(exc_type, fname, exc_tb.tb_lineno)
            break
    print("connection lost")
    del player_map[game_id]

while True:
    conn, addr = s.accept()
    print("connected to", addr)
    if player_id == 0:
        game_id += 1
        game1 = OnlineGameMode(None,game_id,0)
        game2 = copy.deepcopy(game1)
        player_map[game_id] = [game1, game2]
        start_new_thread(connection_thread, (conn, connectionCount, game_id, player_id))
    else:
        start_new_thread(connection_thread, (conn, connectionCount, game_id, player_id))
    
    connectionCount += 1
    player_id = (player_id + 1)%2
