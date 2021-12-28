import sys
import socket
import event_publisher as ep
import threading
import event_generator as eg

server_host = "" # The network interface address, empty value indicates the server is listneing on all of the network interfaces 
server_port = 8001 # The default port number for the server
event_publisher = ep.EventPublisher()

print("Arg length:" + str(len(sys.argv)))
if len(sys.argv) == 3:
    server_host = sys.argv[1]
    server_port = int(sys.argv[2])

print("The server is listening the network interface {0} on port {1}".format(server_host, server_port))

svr_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
svr_socket.bind((server_host, server_port))
svr_socket.listen()

event_generator = eg.EventGenerator(event_publisher)
event_generator_thread = threading.Thread(target=event_generator.generate_test_events, args=())
event_generator_thread.start()

while True:   
    print('Server is listening for the client connection')
    client_socket, client_addr = svr_socket.accept()
    print('Connected client is: ', client_addr)    
    event_publisher.add_socket(client_socket)
    print('Server added client socket to the event publisher')
   