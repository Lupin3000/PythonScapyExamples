#!/usr/bin/env python

import argparse
import signal
from os import system
from sys import exit
from threading import Thread
from time import sleep

from scapy.layers.dot11 import Dot11, Dot11Beacon, Dot11ProbeResp, Dot11ProbeReq, Dot11Elt, sniff, RadioTap


def keyboard_interrupt_handler(interrupt_signal, frame):
    """
    Keyboard (CTRL + C) interrupt function
    """
    print("Scanning finished")
    print("KeyboardInterrupt ID: {} {} has been caught.".format(interrupt_signal, frame))
    exit(1)


def evaluate_sniffing_packet_ap(packet):
    """
    Evaluate wifi packet's and print to terminal

    :param packet: sniffed Wifi packets
    :type packet: class
    """
    start_c = '\33[33m'
    end_c = '\033[0m'

    if packet.haslayer(Dot11Beacon) or packet.haslayer(Dot11ProbeResp):
        if packet.type == 0 and packet.subtype == 8:
            bssid = packet[Dot11].addr2
            ssid = packet[Dot11Elt].info.decode().strip()

            if not ssid:
                ssid = "N/A"

            try:
                dbm = packet.dBm_AntSignal
            except:
                dbm = "N/A"

            stats = packet[Dot11Beacon].network_stats()
            channel = stats.get("channel")
            protocol = stats.get("crypto")
            enc = next(iter(protocol))

            if enc == 'OPN' or enc == 'WEP':
                print(start_c + "{:<24} {:<35} {:<5} {:<7} {}".format(bssid, ssid, dbm, channel, enc) + end_c)
            else:
                print("{:<24} {:<35} {:<5} {:<7} {}".format(bssid, ssid, dbm, channel, enc))


def evaluate_sniffing_packet_sta(packet):

    if packet.haslayer(Dot11ProbeReq) and packet.haslayer(Dot11Elt):
        if packet.type == 0 and packet.subtype == 4:
            mac = packet.addr2
            ssid = packet[Dot11Elt].info.decode().strip()
            rssi = RadioTap.dBm_AntSignal

            if not ssid:
                ssid = "N/A"

            print("STA {} looking for {}".format(mac, ssid))


def set_specific_channel(channel_number):
    """
    Set specific wifi channel

    :param channel_number: channel number
    :type channel_number: int
    """
    global interface

    print("Set channel to {} on interface {}".format(channel_number, interface))
    system(f"iwconfig {interface} channel {channel_number}")


def change_channel():
    """
    Change wifi channels between 1 and 14
    """
    global interface

    print("Change channels for interface {}".format(interface))
    channel_number = 1

    while True:
        system(f"iwconfig {interface} channel {channel_number}")
        channel_number = channel_number % 14 + 1
        sleep(0.5)


def run_app():
    """
    Main function to parse arguments and run
    """
    global interface
    global filter_results

    description = 'Simple Wifi scanner for 2.4 GHz range'
    epilog = 'The author of this code take no responsibility for your use or misuse'
    parser = argparse.ArgumentParser(prog='ScanWifi.py', description=description, epilog=epilog)
    parser.add_argument("interface", help='Your interface in monitor mode')
    parser.add_argument('-c', '--channel', help='Channel number for 2.4 GHz range (min 1/max 14)', default=1, type=int)
    parser.add_argument('--all', help='Scan on all channels for 2.4 GHz range', default=False, action='store_true')
    parser.add_argument('--filter', help='Filter results only for STA (Probe Req)', default=False, action='store_true')
    args = parser.parse_args()

    if len(args.interface) < 1:
        print('You did not provide any interface?')
        exit(1)
    else:
        interface = args.interface

    if not args.all and (args.channel < 1 or args.channel > 14):
        print('You will scan on channel {}?'.format(args.channel))
        exit(1)

    if not args.all and args.channel in range(1, 14):
        set_specific_channel(args.channel)

    if args.all:
        channel_changer = Thread(target=change_channel)
        channel_changer.daemon = True
        channel_changer.start()

    if args.filter:
        print("-" * 85)
        sniff(prn=evaluate_sniffing_packet_sta, iface=interface)
    else:
        print("-" * 85)
        print("{:<24} {:<35} {:<5} {:<7} {}".format("BSSID", "SSID", "dbm", "CH", "ENC"))
        print("-" * 85)
        sniff(prn=evaluate_sniffing_packet_ap, iface=interface)


if __name__ == "__main__":
    interface = filter_results = None
    signal.signal(signal.SIGINT, keyboard_interrupt_handler)
    run_app()
