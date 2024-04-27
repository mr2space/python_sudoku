import socket
import _thread
import os
import pickle


class Network:
    def __init__(self) -> None:
        self.server = ""
        self.port = 5555
        self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.addr = (self.server, self.port)
    
    def connect(self):
        try:
            self.boradObj = self.client.connect(self.addr)
            self.send(self.boradObj)
            return self.boradObj
        except Exception as err:
            print(err)
        return None
    
    def send(self, data):
        try:
            self.client.send(pickle.dumps(data))
            return pickle.loads(self.client.recv(4096))
        except Exception as err:
            print(err)
        
    