import socket
import json

HOST = '127.0.0.1'
PORT = 27972
BUFFER_SIZE = 4096

class TrainSocket:
    def __init__(self, sock=None):
        if sock is None:
            self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        else:
            self.sock = sock

    def __del__(self):
        self.sock.close()

    def connect(self):
        self.sock.connect((HOST, PORT))
        self.sock.sendall(b'/REGISTER-TRAIN-CLIENT')

        data = self.sock.recv(BUFFER_SIZE)
        print('Connection established with host: {}, port: {}'.format(HOST, PORT))

    def get_env_state(self):
        self.sock.send(b'/GET-ENV-STATE')

    def handle_data(self, data):
        print(data)

conn = TrainSocket()
conn.connect()
conn.get_env_state()

# So that the socket is never closed
while True:
    data = conn.sock.recv(BUFFER_SIZE)

    if not data:
        break

    string_env = data.decode()

    conn.handle_data(string_env)

socket.close()

