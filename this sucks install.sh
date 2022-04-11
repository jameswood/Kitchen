#!/bin/bash
sudo apt-get install --no-install-recommends xserver-xorg x11-xserver-utils xinit openbox chromium-browser python3-pip
sudo ln -s ${pwd}/autostart /etc/xdg/openbox/autostart
sudo ln -s ${pwd}/URL /etc/xdg/openbox/environment
ln -s ${pwd}/bash_profile ~/.bash_profile

sudo ln -s ${pwd}/Autobright.service /etc/systemd/system/Autobright.service
pip3 install rpi-backlight
sudo systemctl enable Autobright
sudo systemctl start Autobright
echo "Now reboot"
