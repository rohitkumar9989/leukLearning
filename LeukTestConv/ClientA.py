 
import socket
import sys,os;


SERVER = "127.0.0.1"
PORT = 8080
client1 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client1.connect((SERVER, PORT))
client1.sendall(bytes("Client_B",'UTF-8'))

while True:
  in_data =  client1.recv(1024)
  print("____________________________________From Server :" ,in_data.decode())
  out_data = input()
  client1.sendall(bytes(out_data,'UTF-8'))
  if out_data=='bye':
  	break
client1.close()