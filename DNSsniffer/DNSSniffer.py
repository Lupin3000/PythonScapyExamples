#!/usr/bin/env python

import json
import os
import signal
import sys
from collections import Counter
from datetime import datetime

from scapy.all import sniff
from scapy.layers.dns import DNS
from scapy.layers.inet import IP


def keyboard_interrupt_handler(interrupt_signal, frame):
    """
    Keyboard (CTRL + C) interrupt function
    """
    print("Sniffing finished")
    print("KeyboardInterrupt ID: {} {} has been caught.".format(interrupt_signal, frame))

    if len(stored_dns_requests) > 0:
        target_file = "report.json"

        store_to_file = input("You like to save results to file {} (Y/N)?: ".format(target_file))
        if store_to_file == 'Y':
            with open(target_file, 'w') as file_handler:
                file_handler.write(json.dumps(stored_dns_requests))
                print("Save content into: {}".format(os.path.abspath(target_file)))

        show_top_domains = input("You like to see the top 5 DNSsniffer requests (Y/N)?: ")
        if show_top_domains == 'Y':
            top_domains = Counter(stored_dns_requests.values()).most_common(5)
            for key, value in top_domains:
                print("{:<50}: {}".format(key, value))

    sys.exit(0)


def query_sniff(pkt):
    """
    Scapy DNS filter function
    """
    if IP in pkt:
        ip_src = pkt[IP].src
        ip_dst = pkt[IP].dst
        if pkt.haslayer(DNS) and pkt.getlayer(DNS).qr == 0:
            domain = pkt.getlayer(DNS).qd.qname.decode("utf-8")
            now = datetime.now()
            stored_dns_requests.update({datetime.timestamp(now): domain})
            print("SRC: {} - DST: {} : {}".format(ip_src, ip_dst, domain))


def run_sniffer():
    """
    Scapy packet sniffer function
    """
    interface = input("Enter your interface (eq en0): ")
    print("Sniffing started - press [CTRL] + [c] to interrupt sniffing:")
    sniff(iface=interface, filter="port 53", prn=query_sniff, store=0)


if __name__ == "__main__":
    stored_dns_requests = dict()
    signal.signal(signal.SIGINT, keyboard_interrupt_handler)
    run_sniffer()
