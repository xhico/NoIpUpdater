# NoIpUpdater

## Automates the process of updating NoIp DynDNS

## Installation

```
python3 -m pip install -r /home/pi/NoIpUpdater/requirements.txt --no-cache-dir
sudo apt install firefox-esr -y
```

## Usage

Manual

```
python3 NoIpUpdater.py
```

Crontab (every day at 2am)

```
0 2 * * * python3 /home/pi/NoIpUpdater/NoIpUpdater.py
```

