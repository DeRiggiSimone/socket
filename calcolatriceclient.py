import socket
import json

SERVER_IP="127.0.0.1"
SERVER_PORT=5005
BUFFER_SIZE=1024

s=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
s.bind((SERVER_IP,SERVER_PORT))

while true:
    primoNumero=float(primoNumero)
    operazione=input("inserisci l'operazione (+,-,*,%)")
    secondoNumero=float(input("inserisci il secondo numero"))
    messaggio={'primoNumero':primoNumero,
               'operazione':operazione,
               'secondoNumero':secondoNumero}
    messaggio=json.dumps(messaggio)
    s.sendall(messaggio.encode("UTF-8"))
    data=s.recv(1024)
    print("Risultato: ",data.decode)