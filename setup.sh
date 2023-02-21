#!/bin/bash
echo "1.Linux"
echo "2.Android"
read -p "Enter your OS:" os
case $os in 
  "1") 
  apt update
  apt upgrade
  apt install python3
  pip3 install requests
  pip3 install termcolor
  pip3 install argparse
  ;;
  "2") 
  pkg update
  pkg upgrade
  pkg install python3
  pip3 install requests
  pip3 install termcolor
  pip3 install argparse
  ;;
esac