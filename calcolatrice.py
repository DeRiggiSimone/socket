import socket
import json

SERVER_IP="127.0.0.1"
SERVER_PORT=5005
BUFFER_SIZE=1024

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

while True:
    data=s.recv(1024)
    if not data:
        break
    data=data.decode()
    data=json.loads(data)
    primoNumero=data['primoNumero']
    operazione=data['operazione']
    secondoNumero=data['secondoNumero']