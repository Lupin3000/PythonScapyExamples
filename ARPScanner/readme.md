# ARP Scanner

ARP scanner script to display ARP responses for a specific IP or CIDR

## Prepare environment

- You can use Python virtualenv
- Python3.x is needed
- root rights required (_or via sudo_)

```shell
# install needed packages
$ sudo apt install python3-pip python3-venv

# create and change into Project directory
$ mkdir -p ~/Projects/ARP-Scanner && cd ~/Projects/ARP-Scanner

# create virtualenv
$ virtualenv -p python3 venv
# or
$ python3 -m venv venv

# activate virtualenv
$ . venv/bin/activate

# install requirements
(venv) $ pip install -r requirements.txt
# or
(venv) $ pip install scapy

# list packages (optional)
(venv) $ pip freeze

# make file executable
(venv) $ chmod u+x ARPScanner.py
```

## Run ARP Scanner

just run it...

```shell
# show help (optional)
(venv) $ sudo venv/bin/python ./ARPScanner.py --help

# scan for a specific IP
(venv) $ sudo venv/bin/python ./ARPScanner.py en0 172.20.10.5

# scan network with CIDR
(venv) $ sudo venv/bin/python ./ARPScanner.py en0 172.20.10.1/24
```

to interrupt press [CTRL + c] and follow terminal output.

## Example output

some example from my terminal...

```shell
Start ARP scanning on interface en0 on network 172.20.10.1/24
Begin emission:
Finished sending 256 packets.

Received 313 packets, got 3 answers, remaining 253 packets
IP: 172.20.10.1     MAC: ca:38:b0:d7:41:64
IP: 172.20.10.5     MAC: db:e2:b0:97:91:ac
IP: 172.20.10.11    MAC: c1:02:10:55:04:a2
```

[Go back](../README.md)