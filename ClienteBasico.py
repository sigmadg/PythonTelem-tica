import sys, os
from socket import *
if(len(sys.argv) > 2):
    server_name=sys.argv[1]
    server_port = int(sys.argv[2])
else:
    print ("Uso: python cliente_basico server_name server_port")
    sys.exit(1)
server_address = gethostbyname(server_name)
connection_socket = socket(AF_INET,SOCK_STREAM)
connection_socket.connect((server_address, server_port))
incoming_stream = connection_socket.makefile("rt")
outgoing_stream = connection_socket.makefile("wt")
print (incoming_stream.read())
incoming_stream.close()
outgoing_stream.close()
connection_socket.close()
