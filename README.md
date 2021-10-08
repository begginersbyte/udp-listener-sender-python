# UDP Lister & Sender in python
These scripts, as they name say, can be used to send AND listen for UDP packets.

* sendUDP .py 
    * BASIC script you can use to send messages to a host in one specifc UDP port.
* udplistener .py
    * use this script to listen for udp packets in one specific port and then, store the packets/messages in a .log file to consume it later on.

### Real life usage:
Let's say you have 20 network devices sending UDP packets to a centralized logging system (such as the ELK Stack). What happen if that Centrilized Logging system goes down? All the UDP messages will be lost (you know, regular UDP doing its stuff). To prevent this data loss, you can put the udplistener .py script in a container (_using the Dockerfile to create the corresponding docker image and then the docker-compose.yml file to start up the necessary containers_) and keep listening AND storing those message into .log files. In the scenario that you are using ELK, you can use Filebeat to read the messages from the corresponding .log files and transfer them to Logstash once everything is back to normal.