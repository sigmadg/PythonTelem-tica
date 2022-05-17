import sys, os
from socket import *

if(len(sys.argv) > 2):
    server_name=sys.argv[1]
    server_port = int(sys.argv[2])
else:
    print ("Uso: python cliente_interactivo server_name server_port")
    sys.exit(1)
server_address = gethostbyname(server_name)
connection_socket = socket(AF_INET,SOCK_STREAM)
connection_socket.connect((server_address, server_port))
pid = os.fork()

if pid != 0:
    incoming_stream = connection_socket.makefile("rt")
    print ("El cliente acepta mensajes del servidor")
    while True:
        msg = incoming_stream.readline()
        print (msg)
        if msg == ("salir\n"):
            break
    incoming_stream.close()
    connection_socket.close()

    print ("Servidor desconectado. Si no esta desconectado escriba salir")

    os.waitpid(pid, 0)
else:
    outgoing_stream = connection_socket.makefile("wt")
    print ("El cliente permite mandar mensajes al servidor")
    while True:
        msg = raw_input()
        outgoing_stream.write(msg + "\n")
        outgoing_stream.flush()
        if msg == ("salir"):
            break
    outgoing_stream.close()
    connection_socket.close()
    sys.exit(0)