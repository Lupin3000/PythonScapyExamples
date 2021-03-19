# Set Wi-Fi interface into monitor mode

Script to set specific Wi-Fi interface into monitor mode

## Requirements

- Packages `ip`and `iwconfig` must be installed
- root rights required (_or via sudo_)

_Note:_ [Here](https://softwaretester.info/wifi-monitor-mode-basics/) you will find different other options (_combinations_), to set your interface into monitor mode.

## Run Wi-Fi Scanner

just run it...

```shell
# make file executable
$ chmod u+x monitor-mode.sh
 
# show help (optional)
$ sudo ./monitor-mode.sh -h

# set wlan1 into monitor mode
$ sudo ./monitor-mode.sh -i wlan1
```

## Example output

some example from my terminal...

```shell
[+2021-03-17_20-01-24] [INFO]: wlan1 selected by user
[+2021-03-17_20-01-24] [INFO]: Set interface wlan1 down
[+2021-03-17_20-01-24] [INFO]: Set interface wlan1 mode monitor
[+2021-03-17_20-01-24] [INFO]: Set interface wlan1 up
[+2021-03-17_20-01-24] [INFO]: Interface wlan1 status is Mode:Monitor
```

[Go back](../README.md)