import socket
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

S_IP = config['NETWORK']['SERVER_IP']
S_PORT = int(config['NETWORK']['SERVER_PORT'])
S_ADDR = (S_IP, S_PORT)

C_IP = config['NETWORK']['CLIENT_IP']
C_PORT = int(config['NETWORK']['CLIENT_PORT'])
DATA_DIR = config['ENV']['CLIENT_DATA_PATH']+'/'

s = socket.socket()
s.connect(S_ADDR)
file = open(DATA_DIR+'recieved.bmp', 'wb')
while True:
    data = s.recv(1024)
    if data == b'': break
    file.write(data)
s.close()
