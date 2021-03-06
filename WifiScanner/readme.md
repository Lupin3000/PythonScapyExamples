# Wi-Fi Scanner

Script to scan on 2.4 GHz Wi-Fi's (_if ENC is OPN or WEP the output is colored_). Optional you can scan for STA's only. 

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
$ mkdir -p ~/Projects/WifiScan && cd ~/Projects/WifiScan

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
(venv) $ chmod u+x ScanWifi.py 
```

## Run Wi-Fi Scanner

just run it...

```shell
# show help (optional)
(venv) $ sudo venv/bin/python ./ScanWifi.py --help

# start scanning only on specific channel
(venv) $ sudo venv/bin/python ./ScanWifi.py wlan1 -c 9

# start scanning on all 2.4 GHz channels
(venv) $ sudo venv/bin/python ./ScanWifi.py wlan1 --all

# filter for STA probe requests
(venv) $ sudo venv/bin/python ./ScanWifi.py wlan1 --all --filter
```

to interrupt press [CTRL + c]

## Example output

some example from my terminal...

```shell
Set channel to 6 on interface wlan1
-------------------------------------------------------------------------------------
BSSID                    SSID                                dbm   CH      ENC
-------------------------------------------------------------------------------------
09:3e:5d:34:11:b4        Sunrise_2.4GHz_3411B0               -79   6       WPA/PSK
55:67:51:c3:2c:b4        UPC88417C7                          -68   6       WPA/PSK
8b:30:dc:c2:ea:62        Bose ST Home Thtr (2AB026)          -77   6       OPN
b8:ce:a3:d6:81:d0        Dosmeethelm                         -71   6       WPA2/PSK
54:67:51:3c:2c:b4        UPC88417C7                          -68   6       WPA/PSK
80:30:dc:c2:dd:62        Bose ST Home Thtr (2AB026)          -78   6       OPN
...
```

... with `--filter` to show only Probe Requests ...

```shell
Change channels for interface wlan1
-------------------------------------------------------------------------------------
STA 5c:aa:fd:b4:41:bb looking for Sonos_StdbhVj1gi78Xag6fMBAxKGPsP
STA 45:03:2c:8b:7c:2d looking for N/A
STA f8:0e:f9:36:d2:1c looking for Salt_2GHz_0EE4AE
STA 44:03:2b:4b:7e:2d looking for WuTangLan
```

[Go back](../README.md)
