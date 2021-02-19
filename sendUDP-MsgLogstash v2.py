import socket
import time

#UDP_IP = "LogstashServerHere"
#UDP_PORT = PORTHERE
UDP_IP = "127.0.0.1"
UDP_PORT = 20001

#################################################
# Q931 MESSAGES (5 events)
#################################################
MESSAGE1 = "Jan 15 01:41:24.069: ISDN Se0/0/0:15 Q931: Applying typeplan for sw-type 0x12 is 0x0 0x1, Calling num 7022556"
MESSAGE2 = "Jan 15 01:41:24.071: ISDN Se0/0/0:15 Q931: Sending SETUP  callref = 0x6141 callID = 0xE0C2 switch = primary-net5 interface = User"
MESSAGE3 = "Jan 15 01:41:24.071: ISDN Se0/0/0:15 Q931: TX -> SETUP pd = 8  callref = 0x6141 "
MESSAGE4 = "                Standard = CCITT "
MESSAGE5 = "                Transfer Capability = Speech  "
MESSAGE6 = "                Transfer Mode = Circuit "
MESSAGE7 = "                Transfer Rate = 64 kbit/s "
MESSAGE8 = "        Channel ID i = 0xA98381 "
MESSAGE9 = "                Exclusive, Channel 1 "
MESSAGE10 = "        Calling Party Number i = 0x0181, '7022556' "
MESSAGE11 = "                Plan:ISDN, Type:Unknown "
MESSAGE12 = "        Called Party Number i = 0x81, '10086' "
MESSAGE13 = "                Plan:ISDN, Type:Unknown"
MESSAGE14 = "Jan 15 01:41:24.163: ISDN Se0/0/0:15 Q931: RX <- SETUP_ACK pd = 8  callref = 0xE141 "
MESSAGE15 = "        Channel ID i = 0xA98381 "
MESSAGE16 = "                Exclusive, Channel "
MESSAGE17 = "Jan 15 01:41:32.430: ISDN Se0/0/0:15 Q931: RX <- ALERTING pd = 8  callref = 0xE141 "
MESSAGE18 = "        Progress Ind i = 0x8281 - Call not end-to-end ISDN, may have in-band info  "
MESSAGE19 = "        Progress Ind i = 0x8288 - In-band info or appropriate now available "

#################################################
# SIP MESSAGES (5 events)
#################################################

MESSAGE20 = '661105: Dec  9 07:18:47.029: //2113420/C544D4800002/SIP/Msg/ccsipDisplayMsg:'
MESSAGE21 = 'Sent: '
MESSAGE22 = 'SIP/2.0 100 Trying'
MESSAGE23 = 'Via: SIP/2.0/TCP 172.24.244.15:5060;branch=z9hG4bK232cc0364af19c2'
MESSAGE24 = 'From: "Zonglian Wang" <sip:234513336@172.24.244.15>;tag=181479137~28f81eb0-0abe-4b08-b5d4-c909149c13d4-96775241'
MESSAGE25 = 'To: <sip:00517803906@172.24.51.5>'
MESSAGE26 = 'Date: Wed, 09 Dec 2020 07:18:47 GMT'
MESSAGE27 = 'Call-ID: c544d480-fd017a56-224f141-ff418ac@172.24.244.15'
MESSAGE28 = 'CSeq: 101 INVITE'
MESSAGE29 = 'Allow-Events: telephone-event'
MESSAGE30 = 'Server: Cisco-SIPGateway/IOS-15.3.3.M4'
MESSAGE31 = 'Content-Length: 0'
MESSAGE32 = '661106: Dec  9 07:18:47.033: //2113421/C544D4800002/SIP/Msg/ccsipDisplayMsg:'
MESSAGE33 = 'Received: '
MESSAGE34 = 'SIP/2.0 100 Trying'
MESSAGE35 = 'Via: SIP/2.0/UDP 20.20.20.10:5060;branch=z9hG4bK7D2C48C0'
MESSAGE36 = 'To: <sip:0517803906@20.20.20.20>'
MESSAGE37 = 'From: "Zonglian Wang"<sip:07042424288@20.20.20.10>;tag=BFB3E534-86'
MESSAGE38 = 'Call-ID: 9CB02CC0-392511EB-B858ECAE-843D405@20.20.20.10'
MESSAGE39 = 'CSeq: 101 INVITE'
MESSAGE40 = 'Content-Length: 0'
MESSAGE41 = '661107: Dec  9 07:18:47.165: //-1/xxxxxxxxxxxx/SIP/Msg/ccsipDisplayMsg:'
MESSAGE42 = 'Received: '
MESSAGE43 = 'OPTIONS sip:172.24.244.228:5060 SIP/2.0'
MESSAGE44 = 'Via: SIP/2.0/TCP 172.24.244.16:5060;branch=z9hG4bK16132b825818465'
MESSAGE45 = 'From: <sip:172.24.244.16>;tag=784508409'
MESSAGE46 = 'To: <sip:172.24.244.228>'
MESSAGE47 = 'Date: Wed, 09 Dec 2020 07:18:47 GMT'
MESSAGE48 = 'Call-ID: c5dd6b00-fd017a57-1611f72-10f418ac@172.24.244.16'
MESSAGE49 = 'User-Agent: Cisco-CUCM11.5'
MESSAGE50 = 'CSeq: 101 OPTIONS'
MESSAGE51 = 'Contact: <sip:172.24.244.16:5060;transport=tcp>'
MESSAGE52 = 'Max-Forwards: 0'
MESSAGE53 = 'Content-Length: 0'
MESSAGE54 = '661108: Dec  9 07:18:47.165: //-1/xxxxxxxxxxxx/SIP/Msg/ccsipDisplayMsg:'
MESSAGE55 = 'Sent: '
MESSAGE56 = 'SIP/2.0 200 OK'
MESSAGE57 = 'Via: SIP/2.0/TCP 172.24.244.16:5060;branch=z9hG4bK16132b825818465'
MESSAGE58 = 'From: <sip:172.24.244.16>;tag=784508409'
MESSAGE59 = 'To: <sip:172.24.244.228>;tag=BFB3E5BC-1EB7'
MESSAGE60 = 'Date: Wed, 09 Dec 2020 07:18:47 GMT'
MESSAGE61 = 'Call-ID: c5dd6b00-fd017a57-1611f72-10f418ac@172.24.244.16'
MESSAGE62 = 'Server: Cisco-SIPGateway/IOS-15.3.3.M4'
MESSAGE63 = 'CSeq: 101 OPTIONS'
MESSAGE64 = 'Allow: INVITE, OPTIONS, BYE, CANCEL, ACK, PRACK, UPDATE, REFER, SUBSCRIBE, NOTIFY, INFO, REGISTER'
MESSAGE65 = 'Allow-Events: telephone-event'
MESSAGE66 = 'Accept: application/sdp'
MESSAGE67 = 'Supported: timer,resource-priority,replaces,sdp-anat'
MESSAGE68 = 'Content-Type: application/sdp'
MESSAGE69 = 'Content-Length: 379'
MESSAGE70 = 'v=0'
MESSAGE71 = 'o=CiscoSystemsSIP-GW-UserAgent 2204 4664 IN IP4 172.24.244.228'
MESSAGE72 = 's=SIP Call'
MESSAGE73 = 'c=IN IP4 172.24.244.228'
MESSAGE74 = 't=0 0'
MESSAGE75 = 'm=audio 0 RTP/AVP 18 0 8 9 4 2 15'
MESSAGE76 = 'c=IN IP4 172.24.244.228'
MESSAGE77 = 'm=image 0 udptl t38'
MESSAGE78 = 'c=IN IP4 172.24.244.228'
MESSAGE79 = 'a=T38FaxVersion:0'
MESSAGE80 = 'a=T38MaxBitRate:9600'
MESSAGE81 = 'a=T38FaxRateManagement:transferredTCF'
MESSAGE82 = 'a=T38FaxMaxBuffer:200'
MESSAGE83 = 'a=T38FaxMaxDatagram:320'
MESSAGE84 = 'a=T38FaxUdpEC:t38UDPRedundancy'
MESSAGE85 = '661113: Dec  9 07:18:48.605: //2113421/C544D4800002/SIP/Msg/ccsipDisplayMsg:'
MESSAGE86 = 'Sent: '
MESSAGE87 = 'ACK sip:server@20.20.20.20:5060;transport=UDP SIP/2.0'
MESSAGE88 = 'Via: SIP/2.0/UDP 20.20.20.10:5060;branch=z9hG4bK7D2C51760'
MESSAGE89 = 'From: "Zonglian Wang" <sip:07042424288@20.20.20.10>;tag=BFB3E534-86'
MESSAGE90 = 'To: <sip:0517803906@20.20.20.20>;tag=9d5d1634_7070_utc015c5715345'
MESSAGE91 = 'Date: Wed, 09 Dec 2020 07:18:47 GMT'
MESSAGE92 = 'Call-ID: 9CB02CC0-392511EB-B858ECAE-843D405@20.20.20.10'
MESSAGE93 = 'Max-Forwards: 70'
MESSAGE94 = 'CSeq: 101 ACK'
MESSAGE95 = 'Allow-Events: telephone-event'
MESSAGE96 = 'Content-Length: 0'


#################################################
#SENDING all messages (total 10 events)
#################################################

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # UDP

for x in range(1,97):
    print(eval('MESSAGE'+str(x)))
    sock.sendto(bytes(eval('MESSAGE'+str(x)), "utf-8"), (UDP_IP, UDP_PORT))
    time.sleep(0.5)
