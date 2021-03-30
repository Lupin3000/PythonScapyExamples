# DNS Sniffer

DNS sniffer script to display DNS requests and optional to store DNS requests (_as JSON file with a timestamp_) and/or to show top 5 requests.

## Prepare environment

- You can use Python virtualenv
- Python3.x is needed
- root rights required (_or via sudo_)

```shell
# install needed packages
$ sudo apt install python3-pip python3-venv
# or
$ sudo pip3 install virtualenv

# create and change into Project directory
$ mkdir -p ~/Projects/DNS-Sniffer && cd ~/Projects/DNS-Sniffer

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
(venv) $ chmod u+x DNSSniffer.py
```

## Run DNS Sniffer

just run it...

```shell
# show help (optional)
(venv) $ sudo venv/bin/python ./DNSSniffer.py --help

# run DNS sniffer on interface en11
(venv) $ sudo venv/bin/python ./DNSSniffer.py en11
```

to interrupt press [CTRL + c] and follow terminal output.

## Example output

some example from my terminal...

```shell
Sniffing started - press [CTRL] + [c] to interrupt sniffing:
SRC: 172.20.10.10 - DST: 172.20.10.1 : eu-prod.asyncgw.teams.microsoft.com.
SRC: 172.20.10.10 - DST: 172.20.10.1 : emea.ng.msg.teams.microsoft.com.
SRC: 172.20.10.10 - DST: 172.20.10.1 : pagead2.googlesyndication.com.
SRC: 172.20.10.10 - DST: 172.20.10.1 : outlook.live.com.
SRC: 172.20.10.10 - DST: 172.20.10.1 : go.trouter.skype.com.
SRC: 172.20.10.10 - DST: 172.20.10.1 : azwcus1-client-s.gateway.messenger.live.com.
SRC: 172.20.10.10 - DST: 172.20.10.1 : lpcres.delve.office.com.
SRC: 172.20.10.10 - DST: 172.20.10.1 : safebrowsing.googleapis.com.
SRC: 172.20.10.10 - DST: 172.20.10.1 : storage.live.com.
...
SRC: 172.20.10.10 - DST: 172.20.10.1 : pr.ybp.yahoo.com.
SRC: 172.20.10.10 - DST: 172.20.10.1 : s.yimg.com.
SRC: 172.20.10.10 - DST: 172.20.10.1 : beap-bc.yahoo.com.
Sniffing finished
KeyboardInterrupt ID: 2 <frame at 0x7fa448c7b620, file '/Users/lupin/Desktop/myTest/venv/lib/python3.7/site-packages/scapy/arch/bpf/supersocket.py', line 420, code bpf_select> has been caught.
You like to save results to file report.json (Y/N)?: Y
Save content into: /Users/lupin/Desktop/myTest/report.json
You like to see the top 5 DNSsniffer requests (Y/N)?: Y
eu-prod.asyncgw.teams.microsoft.com.              : 22
emea.ng.msg.teams.microsoft.com.                  : 15
pagead2.googlesyndication.com.                    : 7
outlook.live.com.                                 : 5
go.trouter.skype.com.                             : 2
```

[Go back](../README.md)
