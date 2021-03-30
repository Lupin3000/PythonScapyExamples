#!/usr/bin/env python

import argparse
import signal
from sys import exit

from scapy.layers.inet import TCP, IP, sr1


def keyboard_interrupt_handler(interrupt_signal, frame):
    """
    Keyboard (CTRL + C) interrupt function
    """
    print("Scanning finished")
    print("KeyboardInterrupt ID: {} {} has been caught.".format(interrupt_signal, frame))
    exit(1)


def port_scan(network, port, show_negative):
    """
    Port scan function

    :param network: target network
    :type network: str
    :param port: port
    :type port: int
    :param show_negative: show closed ports
    :type show_negative: bool
    """
    res = sr1(IP(dst=network) / TCP(dport=port), verbose=False, timeout=0.2)
    if res is not None and TCP in res:
        if res[TCP].flags == 18:
            print("Port {} is open".format(port))
    else:
        if show_negative:
            print("Port {} seems closed".format(port))


def run_app():
    """
    Main function to parse arguments and run
    """
    target = None
    negative_results = False

    description = 'Simple TCP port scanner'
    epilog = 'The author of this code take no responsibility for your use or misuse'
    parser = argparse.ArgumentParser(prog='TCPPortScan.py', description=description, epilog=epilog)
    parser.add_argument("target", help="Your target to scan")
    parser.add_argument('-p', '--port', help="Set a single port", default=22, type=int)
    parser.add_argument('-r', '--range', help="Set a port range (eq 22-80)")
    parser.add_argument("--all", help="Show negative results (closed ports)", action="store_true")
    args = parser.parse_args()

    if len(args.target) < 1:
        print('You did not provide any target?')
        exit(1)
    else:
        target = args.target

    if args.all:
        negative_results = True

    if args.range:
        print("Start scanning ports {} on target {}".format(args.range, target))
        range_list = args.range.split('-')
        for element in range(int(range_list[0]), int(range_list[1]) + 1):
            port_scan(target, element, negative_results)
    else:
        print("Start scanning port {} on target {}".format(args.port, target))
        port_scan(target, args.port, negative_results)


if __name__ == "__main__":
    signal.signal(signal.SIGINT, keyboard_interrupt_handler)
    run_app()
