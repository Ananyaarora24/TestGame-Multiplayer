import socket 

class Network:
    def __init__(self):
        self.client = socket.socket (socket.AF_INET, socket.SOCK_STREAM)
        self.server = "localhost"
        self.port = 5555
        self.addr = (self.server, self.port)
        self.position = self.connect()
    
    def get_position(self):
        return self.position

    def connect(self):
        try:
            self.client.connect(self.addr)
            return self.client.recv(2043).decode()
        except:
            pass

    def send(self, data):
        try:
            self.client.send(str.encode(data))
            return self.client.recv(2043).decode()
        except socket.error as n:
            print(n)
