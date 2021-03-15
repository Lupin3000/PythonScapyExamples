# DNS Sniffer

Simple Python DNS sniffer script (_via Python Scapy_) to display DNS requests and optional to store DNS requests (_as JSON_) with timestamp and to show top 5.

## Prepare environment

```shell
# create Project directory
$ mkdir -p ~/Projects/DNS-Sniffer && cd ~/Projects/DNS-Sniffer

# create virtualenv
$ virtualenv -p python3 venv

# activate virtualenv
$ . venv/bin/activate

# install requirements
$ pip install -r requirements.txt
```

## Run DNS Sniffer

```shell
# execute python DNS sniffer script
$ python dns_sniff.py
```

to interrupt press [CTRL + c] and follow terminal output.
