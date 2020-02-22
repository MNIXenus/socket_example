import socket
import config
import configparser
import os
from typing import Any, Tuple

config = configparser.ConfigParser()
print('Reading configuration file...', end='')

config.read('config.ini')
print('OK')

print('Reading server network configuration...', end='')
S_IP = config['NETWORK']['SERVER_IP']
S_PORT = int(config['NETWORK']['SERVER_PORT'])
S_ADDR: Tuple[str, int] = (S_IP, S_PORT)
print('OK')

print('Reading server environment configuration...', end='')
DATA_DIR = config['ENV']['SERVER_DATA_PATH']+'/'
print('OK')

print('Creating socket...')
s = socket.socket()
s.bind(S_ADDR)
print(f'Socket successfully created at {S_IP}:{S_PORT}.')
print('listening incoming connections...')
s.listen(1)
while True:
    conn, addr = s.accept()
    print(f'Incoming connection from {addr[0]}:{addr[1]}.')
    file = open(DATA_DIR+'cEdDG.bmp', 'rb')
    conn.sendfile(file)
    print('File sended.')
    file.close()
    conn.close()