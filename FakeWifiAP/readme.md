# Wi-Fi Fake AP

Script to create fake access points, similar to mdk3 or mdk4.

_Note:_ AP's are just fake and STA's cannot connect!!!

## Prepare environment

- you can use Python virtualenv
- Python3.x is needed
- Wi-Fi interface must be in "Monitor Mode" (_you can read [here](https://softwaretester.info/wifi-monitor-mode-basics/) how to do_)
- root rights required (_or via sudo_)

```shell
# install needed packages
$ sudo apt install python3-pip python3-venv
# or
$ sudo pip3 install virtualenv

# create and change into Project directory
$ mkdir -p ~/Projects/FakeWifi && cd ~/Projects/FakeWifi

# create virtualenv
$ virtualenv -p python3 venv
# or
$ python3 -m venv venv

# activate virtualenv
$ . venv/bin/activate

# install requirements
(venv) $ pip install -r requirements.txt
# or
(venv) $ pip install Faker scapy

# list packages (optional)
(venv) $ pip freeze

# make file executable
(venv) $ chmod u+x FakeWifiAP.py 
```

## Run Fake Wi-Fi AP

just run it...

```shell
# show help (optional)
(venv) $ sudo venv/bin/python ./FakeWifiAP.py --help

# create only 1 fake AP
(venv) $ sudo venv/bin/python ./FakeWifiAP.py wlan1

# create 10 fake AP's
(venv) $ sudo venv/bin/python ./FakeWifiAP.py wlan1 -n 10
```

to interrupt press [CTRL + c]

## Example output

some example from my terminal...

```shell
Following AP's are created (CTRL + c to stop):
AP:hall - mac:40:35:b0:18:9a:70
AP:nguyen - mac:57:8b:74:a3:d5:1c
AP:shaw-brown - mac:4e:e1:b5:42:20:17
AP:wiley-johnson - mac:52:99:2f:34:b1:9e
AP:cooper - mac:f6:d4:84:61:d9:5e
```

[Go back](../README.md)
