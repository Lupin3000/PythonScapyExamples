# Wi-Fi Deauthentication

Script to deauthenticate Wi-Fi connections.

## Prepare environment

- you can use Python virtualenv
- Python3.x is needed
- Wi-Fi interface must be in "Monitor Mode" (_you can read [here](https://softwaretester.info/wifi-monitor-mode-basics/) how to do_)
- root rights required (_or via sudo_)

```shell
# install needed packages
$ sudo apt install python3-pip python3-venv

# create and change into Project directory
$ mkdir -p ~/Projects/WifiDeauth && cd ~/Projects/WifiDeauth

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
(venv) $ chmod u+x WifiDeauth.py 
```

## Run Wi-Fi Deauthenticator

just run it...

```shell
... to be done ...
```

to interrupt press [CTRL + c]

## Example output

some example from my terminal...

```shell
... to be done ...
```

[Go back](../README.md)
