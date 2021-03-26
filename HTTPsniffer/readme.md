# HTTP Sniffer

Script to sniff HTTP traffic. Optional to change port and/or show POST raw data

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
$ mkdir -p ~/Projects/HTTPsniffer && cd ~/Projects/HTTPsniffer

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
(venv) $ chmod u+x HTTPsniffer.py
```

## Run HTTP Sniffer

just run it...

```shell
# show help (optional)
(venv) $ sudo venv/bin/python ./HTTPsniffer.py --help

# start HTTP sniffing on specific interface
(venv) $ sudo venv/bin/python ./HTTPsniffer.py en0

# start HTTP sniffing on specific interface and port
(venv) $ sudo venv/bin/python ./HTTPsniffer.py en0 -p 8080

# start HTTP sniffing on specific interface and show POST raw data
(venv) $ sudo venv/bin/python ./HTTPsniffer.py en0 --raw
```

to interrupt press [CTRL + c]

## Example output

some example from my terminal...

```shell
Start HTTP sniffing on port 80 and interface en11
IP: 172.20.10.10         Method: POST URL: ptsv2.com/t/uxo1m-1616314592/edit
AuthUsername=exampleuser
AuthPassword=mysecretpassword
ResponseCode=200
ResponseBody=Thank+you+for+this+dump.+I+hope+you+have+a+lovely+day%21
ResponseDelay=0
IP: 172.20.10.10         Method: GET  URL: ptsv2.com/t/uxo1m-1616314592
...
```

[Go back](../README.md)
