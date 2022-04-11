#!/bin/bash
sudo ln -s ${pwd}/autostart /etc/xdg/openbox/autostart
sudo ln -s ${pwd}/URL /etc/xdg/openbox/environment
ln -s ${pwd}/bash_profile ~/.bash_profile

sudo ln -s ${pwd}/Autobright.service /etc/systemd/system/Autobright.service
sudo systemctl enable Autobright
sudo systemctl start Autobright