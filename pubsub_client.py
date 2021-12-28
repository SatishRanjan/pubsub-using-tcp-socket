import socket
from urllib.parse import urlparse
import sys

# default port number and hostname of the pubsub server
server_host = "localhost"
server_port = 8001

print("Arg length:" + str(len(sys.argv)))
if len(sys.argv) == 3:
    server_host = str(sys.argv[1])
    server_port = int(sys.argv[2])    

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

print("Pubsub server Host: " + server_host)
print("Port: " + str(server_port))
# set up TCP connection to the pubsub server
s.connect((server_host, server_port))

print("Connected to the pubsub sever as subscriber the events")

# Keep running the client with the connected socket to receive the published events from the server
BUFF_SIZE = 4096
data = b''
while True:
    try:
        part = s.recv(BUFF_SIZE)
        data += part
        if not part or len(part) < BUFF_SIZE:
            if data != b'':
                print("Event received, event data: " + data.decode("utf8"))          
            data = b''
    except:
        print("Sever socket connection is broken, closing the client socket") 
        s.close()
        break


