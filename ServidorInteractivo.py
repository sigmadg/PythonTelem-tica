import sys, os
from socket import *
if(len(sys.argv) > 1):
  port = int(sys.argv[1])
else:
  print ("Uso: python servidor_interactivo server_port")
  sys.exit(1)
listening_socket = socket(AF_INET, SOCK_STREAM)
listening_socket.bind(('', port))
listening_socket.listen(1)
accepted_socket, address = listening_socket.accept()
pid = os.fork()

if pid != 0:
 listening_socket.close()
 incoming_stream = accepted_socket.makefile("rt")
 print ("El servidor acepta mensajes del cliente")
 while True:
  msg = incoming_stream.readline()
  print (msg)
  if msg == "salir\n":
   break
 incoming_stream.close()
 accepted_socket.close()

 print ("Cliente desconectado. Si no esta desconectado escriba salir")
 os.waitpid(pid, 0)
else:
 listening_socket.close()
 outgoing_stream = accepted_socket.makefile("wt")
 print ("El servidor permite mandar mensajes al cliente")
 while True:
  msg = raw_input()
  outgoing_stream.write(msg + "\n")
  outgoing_stream.flush()
  if msg == ("salir"):
   break
 outgoing_stream.close()
 accepted_socket.close()
 sys.exit(0)
