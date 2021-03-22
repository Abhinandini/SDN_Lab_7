from scapy.contrib import openflow3
import os
from scapy.all import *


#def mininet():
    #os.system("sudo ovs-vsctl show")
    #return

def values():
    os.system("sudo ovs-vsctl show")
    Controller_IP = input("\n Enter the Controller IP: ")
    sport = int(input ("\n Enter the Switch Port: "))
    dport = int(input ("\n Enter the Controller Port: "))
    for i in range (1,1000):
       #pkt = Ether()/IP(dst=Controller_IP)/TCP(dport=dport)/"OpenFlow 1.3"/"Data"/Ether()/IP()/ICMP()
       # sendp((pkt), iface = "eth0", count=1000)
        sendp(Ether(src='08:00:27:2d:38:eb',dst='08:00:27:76:48:cb',type= 0x0800)/IP(src='192.168.56.101',dst=Controller_IP)/TCP(sport=sport,dport=dport,seq=i)/openflow3.OFPTPacketIn(), iface="eth0")
    

if __name__ == "__main__":
    values()
