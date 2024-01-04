#!/bin/bash
echo "Hello World"
cd /home/pi/bcvp
git stash
git pull
python3 script.py
