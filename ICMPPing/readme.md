# ICMP ping

Super simple ICMP ping implementation

## Prepare environment

- You can use Python virtualenv
- Python3.x is needed
- root rights required (_or via sudo_)

```shell
# install needed packages
$ sudo apt install python3-pip python3-venv

# create and change into Project directory
$ mkdir -p ~/Projects/ICMP-Ping && cd ~/Projects/ICMP-Ping

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
(venv) $ chmod u+x ICMPping.py
```

## Run ICMP ping

just run it...

```shell
# show help (optional)
(venv) $ sudo venv/bin/python ./ICMPping.py --help

# scan for a specific IP
(venv) $ sudo venv/bin/python ./ICMPping.py en11 172.20.10.1
```

## Example output

some example from my terminal...

```shell
Start ICMP ping on interface en11 on network 172.20.10.1
Begin emission:
Finished sending 1 packets.

Received 4 packets, got 1 answers, remaining 0 packets
172.20.10.1 is alive
```

[Go back](../README.md)
