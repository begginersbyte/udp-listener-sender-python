import socket
import os

UDP_IP = "0.0.0.0"
#UDP_PORT = int(os.environ['UDPPORT']) #used in docker to specify the port. If needed comment the line below (-e UDPPORT=4444)
UDP_PORT   = 20001
bufferSize  = 1024

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((UDP_IP, UDP_PORT))

while True:
    bytesAddressPair = sock.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    clientMsg = "{}".format(message)[2:-1] #format data, remove first 2 and last characters
    f=open("output.log", "a") #open/create file to store messages
    f.write(clientMsg + "\n") #write messages to file
    f.flush()
