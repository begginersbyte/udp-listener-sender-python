import socket
import time

UDP_IP = "127.0.0.1"
UDP_PORT = 20001 #Change this port to whatever is the one you want to send test data

#################### MESSAGES ####################
MESSAGE1 = "Jan 15 01:41:24.069: ISDN Se0/0/0:15 Q931: Applying typeplan for sw-type 0x12 is 0x0 0x1, Calling num 7022556"
MESSAGE2 = "Jan 15 01:41:24.071: ISDN Se0/0/0:15 Q931: Sending SETUP  callref = 0x6141 callID = 0xE0C2 switch = primary-net5"
MESSAGE3 = "Jan 15 01:41:24.071: ISDN Se0/0/0:15 Q931: TX -> SETUP pd = 8  callref = 0x6141"
MESSAGE4 = "Standard = CCITT"
MESSAGE5 = "Transfer Capability = Speech"

#################### SENDING all messages ####################
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP

for x in range(1,97):
    print(eval('MESSAGE'+str(x)))
    sock.sendto(bytes(eval('MESSAGE'+str(x)), "utf-8"), (UDP_IP, UDP_PORT))
#    time.sleep(0.5) 