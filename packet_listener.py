import scapy.all as scapy
from scapy_http import http

def packet_listeners(interface):
    scapy.sniff(iface=interface,store=False,prn=analyze_packet)

def analyze_packet(packet):
    packet.show()

packet_listeners("eth0")