# TCP/SYN Traceroute

Script to a TCP/SYN traceroute.

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
$ mkdir -p ~/Projects/TCPSYNTraceroute && cd ~/Projects/TCPSYNTraceroute

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
(venv) $ chmod u+x TCPSYNTraceroute.py
```

## Run TCP/SYN Traceroute

just run it...

```shell
# show help (optional)
(venv) $ sudo venv/bin/python ./TCPSYNTraceroute.py --help

# start traceroute
(venv) $ sudo venv/bin/python ./TCPSYNTraceroute.py example.com
```

to interrupt press [CTRL + c]

## Example output

some example from my terminal...

```shell
Start traceroute to target example.com
Begin emission:
Finished sending 30 packets.
...*......*..............................*.*.**.**..*.***..**.*.*..................................
Received 99 packets, got 16 answers, remaining 14 packets
   93.184.216.34:tcp80 
1  172.20.10.1     11  
2  10.155.144.1    11  
17 93.184.216.34   SA  
18 93.184.216.34   SA  
19 93.184.216.34   SA  
20 93.184.216.34   SA  
21 93.184.216.34   SA  
22 93.184.216.34   SA  
23 93.184.216.34   SA  
24 93.184.216.34   SA  
25 93.184.216.34   SA  
26 93.184.216.34   SA  
27 93.184.216.34   SA  
28 93.184.216.34   SA  
29 93.184.216.34   SA  
30 93.184.216.34   SA
```

[Go back](../README.md)
