import sys, os
from socket import *
from time import *
if(len(sys.argv) > 1):
 port = int(sys.argv[1])
else:
    print ("Uso: python servidor_basico server_port")
    sys.exit(1)
listening_socket = socket(AF_INET,SOCK_STREAM)
listening_socket.bind(('', port))
listening_socket.listen(1)
while 1:
    accepted_socket, address = listening_socket.accept()
    incoming_stream = accepted_socket.makefile("rt")
    outgoing_stream = accepted_socket.makefile("wt")
    local_time = ctime()
    outgoing_stream.write(local_time + "\n")
    print ("Conexion desde", address, "en", local_time)
    incoming_stream.close()
    outgoing_stream.close()
    accepted_socket.close()
