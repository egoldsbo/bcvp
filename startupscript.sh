#!/bin/bash
echo "Hello World"
cd /home/pi/bcvp
git stash
sudo git pull
python3 script.py
