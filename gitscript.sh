#!/bin/bash
cd /home/pi/bcvp
sudo git config --global --add safe.directory /home/pi/bcvp
sudo git stash
sudo git pull
sudo chmod +x /home/pi/bcvp/startupscript.sh
sudo chmod +x /home/pi/bcvp/script.py
sudo chmod +x /home/pi/bcvp/gitscript.sh
sudo chmod +x /home/pi/bcvp/configon.sh
sudo chmod +x /home/pi/bcvp/configoff.sh
