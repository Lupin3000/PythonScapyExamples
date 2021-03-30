#!/usr/bin/env python

import argparse
import signal
from sys import exit

from scapy.layers.inet import traceroute


def keyboard_interrupt_handler(interrupt_signal, frame):
    """
    Keyboard (CTRL + C) interrupt function
    """
    print("Traceroute stopped")
    print("KeyboardInterrupt ID: {} {} has been caught.".format(interrupt_signal, frame))
    exit(1)


def run_traceroute(target):
    """
    Traceroute function

    :param target: target
    :type target: str
    """
    traceroute(target)


def run_app():
    """
    Main function to parse arguments and run
    """
    description = 'TCP/SYN Traceroute script'
    epilog = 'The author of this code take no responsibility for your use or misuse'
    parser = argparse.ArgumentParser(prog='TCPSYNTraceroute.py', description=description, epilog=epilog)
    parser.add_argument("target", help="Your target to reach")
    args = parser.parse_args()

    if len(args.target) < 1:
        print('You did not provide any target?')
        exit(1)
    else:
        print("Start traceroute to target {}".format(args.target))
        run_traceroute(args.target)


if __name__ == "__main__":
    signal.signal(signal.SIGINT, keyboard_interrupt_handler)
    run_app()
