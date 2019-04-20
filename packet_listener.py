import scapy.all as scapy
from scapy_http import http

def packet_listeners(interface):
    scapy.sniff(iface=interface,store=False,prn=analyze_packet)

def analyze_packet(packet):
    if (packet.haslayer(http.HTTPRequest)):
        if (packet.haslayer(scapy.Raw)):
            print(packet[scapy.Raw].load)

packet_listeners("eth0")