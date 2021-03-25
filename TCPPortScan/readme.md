# TCP Port Scanner

Script to scan (_via TCP_) ports. Optional to set a range or single port and/or to show closed ports.

## Prepare environment

- you can use Python virtualenv
- Python3.x is needed
- root rights required (_or via sudo_)

```shell
# install needed packages
$ sudo apt install python3-pip python3-venv

# create and change into Project directory
$ mkdir -p ~/Projects/TCPPortScanner && cd ~/Projects/TCPPortScanner

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
(venv) $ chmod u+x TCPPortScan.py
```

## Run HTTP Sniffer

just run it...

```shell
# show help (optional)
(venv) $ sudo venv/bin/python ./TCPPortScan.py --help

# start single port scan
(venv) $ sudo venv/bin/python ./TCPPortScan.py mydomain.tld -p 80

# start single port scan and show closed
(venv) $ sudo venv/bin/python ./TCPPortScan.py mydomain.tld -p 443 --all

# start port scan of range and show closed
(venv) $ sudo venv/bin/python ./TCPPortScan.py mydomain.tld -r 22-443 --all
```

to interrupt press [CTRL + c]

## Example output

some example from my terminal...

```shell
Start scanning port 80 on target example.com
Port 80 is open
```

[Go back](../README.md)
