#!/usr/bin/env python

import argparse
import signal
from sys import exit

from scapy.layers.inet import IP, ICMP, sr, conf


def keyboard_interrupt_handler(interrupt_signal, frame):
    """
    Keyboard (CTRL + C) interrupt function
    """
    print("Ping stopped")
    print("KeyboardInterrupt ID: {} {} has been caught.".format(interrupt_signal, frame))
    exit(1)


def icmp_ping():
    """
    Ping function
    """
    global interface
    global network

    conf.iface = interface
    conf.verb = 1
    ans, uans = sr(IP(dst=network)/ICMP())
    ans.summary(lambda s, r: r.sprintf("%IP.src% is alive"))


def run_app():
    """
    Main function to parse arguments and run
    """
    global interface
    global network

    description = 'Simple ICMP ping'
    epilog = 'The author of this code take no responsibility for your use or misuse'
    parser = argparse.ArgumentParser(prog='ICMPping.py', description=description, epilog=epilog)
    parser.add_argument("interface", help="Your interface")
    parser.add_argument("network", help="Your target ip")
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

    print("Start ICMP ping on interface {} on network {}".format(interface, network))
    icmp_ping()


if __name__ == "__main__":
    interface = network = None
    signal.signal(signal.SIGINT, keyboard_interrupt_handler)
    run_app()
