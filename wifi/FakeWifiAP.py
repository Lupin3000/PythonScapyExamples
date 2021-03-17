import argparse
from sys import exit
from threading import Thread

from faker import Faker
from scapy.layers.dot11 import Dot11, Dot11Beacon, Dot11Elt, RadioTap, sendp


def create_fake_data(count):
    """
    Create fake data for SSID and mac address

    :param count: number for fake AP's
    :type count: int
    :return: list
    """
    faker = Faker()
    fake_data = [(faker.domain_word(), faker.mac_address()) for i in range(int(count))]
    return fake_data


def send_wifi_beacon(wifi_ssid, ap_mac, interface):
    """
    Separate thread for each AP

    :param wifi_ssid: name of SSID
    :type wifi_ssid: str
    :param ap_mac: value for mac address
    :type ap_mac: str
    :param interface: interface in monitor mode
    :type interface: str
    """
    print("AP:{} - mac:{}".format(wifi_ssid, ap_mac))
    dot11 = Dot11(type=0, subtype=8, addr1="ff:ff:ff:ff:ff:ff", addr2=ap_mac, addr3=ap_mac)
    beacon = Dot11Beacon(cap="ESS+privacy")
    essid = Dot11Elt(ID="SSID", info=wifi_ssid, len=len(wifi_ssid))
    frame = RadioTap()/dot11/beacon/essid
    sendp(frame, inter=0.1, loop=1, iface=interface, verbose=0)


def run_app():
    """
    Main function to parse arguments and run
    """
    description = 'Simple Wifi AP faker'
    epilog = 'The author of this code take no responsibility for your use or misuse'
    parser = argparse.ArgumentParser(prog='FakeWifiAP.py', description=description, epilog=epilog)
    parser.add_argument("interface", help="Your interface in monitor mode")
    parser.add_argument('-n', '--number', help='Number of fake AP\'s', default=1, type=int)
    args = parser.parse_args()

    if len(args.interface) < 1:
        print('You did not provide any interface?')
        exit(1)

    if args.number == 0:
        print('You will have 0 AP\'s?')
        exit(1)

    fake_ssids = create_fake_data(args.number)
    print('Following AP\'s are created (CTRL + c to stop):')
    for ssid, mac in fake_ssids:
        Thread(target=send_wifi_beacon, args=(ssid, mac, args.interface)).start()


if __name__ == "__main__":
    run_app()
