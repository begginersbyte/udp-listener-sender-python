import socket
import os

UDP_IP = "0.0.0.0" #listen to any trafic on the host
UDP_PORT = int(os.environ['UDP_PORT']) #Create an environment variable called UDP_PORT and specify the port number(-e UDP_PORT=4444)
BUFFER_SIZE  = int(os.environ['BUFFER_SIZE'])#Create an environment variable called BUFFER_SIZE and specify it (-e BUFFER_SIZE=1024)

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
    bytesAddressPair = sock.recvfrom(BUFFER_SIZE)
    message = bytesAddressPair[0]
    clientMsg = message.decode("utf-8") #format data, decode utf-8
    f=open(f"./logs/{UDP_PORT}.log", "a") #open/create file to store messages. The name of the file is the port of the Container
    f.write(clientMsg) #write messages to file
    f.flush()
