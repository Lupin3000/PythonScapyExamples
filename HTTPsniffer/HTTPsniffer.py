#!/usr/bin/env python

import argparse
import signal
from sys import exit

from scapy.all import sniff
from scapy.layers.http import HTTPRequest, Raw
from scapy.layers.inet import IP


def keyboard_interrupt_handler(interrupt_signal, frame):
    """
    Keyboard (CTRL + C) interrupt function
    """
    print("HTTP sniffing finished")
    print("KeyboardInterrupt ID: {} {} has been caught.".format(interrupt_signal, frame))
    exit(0)


def http_sniff(packet):
    global raw

    if packet.haslayer(HTTPRequest):
        url = packet[HTTPRequest].Host.decode() + packet[HTTPRequest].Path.decode()
        ip = packet[IP].src
        method = packet[HTTPRequest].Method.decode()

        print("IP: {:<20} Method: {:<4} URL: {}".format(ip, method, url))
        if raw and packet.haslayer(Raw) and method == "POST":
            data = packet[Raw].load.decode().split("&")
            for element in data:
                print(element)


def run_app():
    global interface
    global port
    global raw

    description = 'HTTP sniffer'
    epilog = 'The author of this code take no responsibility for your use or misuse'
    parser = argparse.ArgumentParser(prog='HTTPsniffer.py', description=description, epilog=epilog)
    parser.add_argument('interface', help='Interface you will use (eq en0)')
    parser.add_argument('-p', '--port', help='Port you will use (eq 80 or 8080)', default=80, type=int)
    parser.add_argument("--raw", help="Show POST raw data", action="store_true")
    args = parser.parse_args()

    if args.raw:
        raw = True

    if not args.port:
        port = "port 80"
    else:
        port = "port " + str(args.port)

    if len(args.interface) < 1:
        print('You did not provide any interface?')
        exit(1)

    print("Start HTTP sniffing on port {} and interface {}".format(args.port, args.interface))
    sniff(filter=port, prn=http_sniff, iface=args.interface, store=False)


if __name__ == "__main__":
    interface = port = raw = None
    signal.signal(signal.SIGINT, keyboard_interrupt_handler)
    run_app()
