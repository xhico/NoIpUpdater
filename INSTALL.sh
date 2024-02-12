#!/bin/bash

sudo mv /home/pi/NoIpUpdater/NoIpUpdater.service /etc/systemd/system/ && sudo systemctl daemon-reload
python3 -m pip install -r /home/pi/NoIpUpdater/requirements.txt --no-cache-dir
sudo apt install firefox-esr -y
chmod +x -R /home/pi/NoIpUpdater/*