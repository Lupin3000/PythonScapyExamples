#!/usr/bin/env python

import argparse
import signal
from sys import exit

from scapy.layers.l2 import Ether, ARP, srp, conf


def keyboard_interrupt_handler(interrupt_signal, frame):
    """
    Keyboard (CTRL + C) interrupt function
    """
    print("Scanning stopped")
    print("KeyboardInterrupt ID: {} {} has been caught.".format(interrupt_signal, frame))
    exit(1)


def arp_scan():
    """
    Scanning function
    """
    global interface
    global network

    conf.verb = 1
    ans, uans = srp(Ether(dst="ff:ff:ff:ff:ff:ff")/ARP(pdst=network), timeout=3, iface=interface, inter=0.1)

    for snd, rcv in ans:
        print("IP: {:<15} MAC: {}".format(rcv.psrc, rcv.hwsrc))


def run_app():
    """
    Main function to parse arguments and run
    """
    global interface
    global network

    description = 'Simple ARP scanner'
    epilog = 'The author of this code take no responsibility for your use or misuse'
    parser = argparse.ArgumentParser(prog='ARPScanner.py', description=description, epilog=epilog)
    parser.add_argument("interface", help="Your interface")
    parser.add_argument("network", help="Your target ip or network CIDR")
    args = parser.parse_args()

    if len(args.interface) < 1:
        print('You did not provide any interface?')
        exit(1)
    else:
        interface = args.interface

    if len(args.network) < 1:
        print('You did not provide any ip range?')
        exit(1)
    else:
        network = args.network

    print("Start ARP scanning on interface {} on network {}".format(interface, network))
    arp_scan()


if __name__ == "__main__":
    interface = network = None
    signal.signal(signal.SIGINT, keyboard_interrupt_handler)
    run_app()
