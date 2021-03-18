import argparse
from os import system
from sys import exit
from threading import Thread
from time import sleep

from scapy.layers.dot11 import Dot11, Dot11Beacon, Dot11Elt, sniff


def evaluate_sniffing_packet(packet):
    """
    Evaluate wifi packet's and print to terminal

    :param packet: sniffed Wifi packets
    :type packet: class
    """
    if packet.haslayer(Dot11Beacon):
        bssid = packet[Dot11].addr2
        ssid = packet[Dot11Elt].info.decode()
        try:
            dbm = packet.dBm_AntSignal
        except:
            dbm = "N/A"
        stats = packet[Dot11Beacon].network_stats()
        channel = stats.get("channel")
        protocol = stats.get("crypto")

        print("mac:{} ssid:{} dbm:{} channel:{} protocol:{}".format(bssid, ssid, dbm, channel, protocol))


def set_specific_channel(interface, channel_number):
    """
    Set specific wifi channel

    :param interface: interface in monitor mode
    :type interface: str
    :param channel_number: channel number
    :type channel_number: int
    """
    print("Set channel to {} on interface {}".format(channel_number, interface))
    system(f"iwconfig {interface} channel {channel_number}")


def change_channel(interface):
    """
    Change wifi channels between 1 and 14

    :param interface: interface in monitor mode
    :type interface: str
    """
    print("Change channels for interface {}".format(interface))
    channel = 1
    while True:
        system(f"iwconfig {interface} channel {channel}")
        channel = channel % 14 + 1
        sleep(0.5)


def run_app():
    """
    Main function to parse arguments and run
    """
    description = 'Simple Wifi scanner for 2.4 GHz range'
    epilog = 'The author of this code take no responsibility for your use or misuse'
    parser = argparse.ArgumentParser(prog='ScanWifi.py', description=description, epilog=epilog)
    parser.add_argument("interface", help="Your interface in monitor mode")
    parser.add_argument('-c', '--channel', help='Channel number for 2.4 GHz range (min 1/max 14)', default=1, type=int)
    parser.add_argument('--all', help='Scan on all channels for 2.4 GHz range', default=False, action='store_true')
    args = parser.parse_args()

    if len(args.interface) < 1:
        print('You did not provide any interface?')
        exit(1)

    if not args.all and (args.channel < 1 or args.channel > 14):
        print('You will scan on channel {}?'.format(args.channel))
        exit(1)

    if not args.all and args.channel in range(1, 14):
        set_specific_channel(args.interface, args.channel)

    if args.all:
        channel_changer = Thread(target=change_channel)
        channel_changer.daemon = True
        channel_changer.start()

    sniff(prn=evaluate_sniffing_packet, iface=args.interface)


if __name__ == "__main__":
    run_app()
