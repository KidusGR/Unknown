#!/usr/bin/env bash
#Install Unknown

username=$(whoami)

sudo pip3 install -r ./requirments.txt
sudo mkdir -p /home/$username/.UnknownData/ && sudo touch /home/$username/.UnknownData/words && sudo chmod u+x ./Unknown.py && sudo cp Unknown.py /usr/local/bin/Unknown && echo -e "\n\nNow just run\n$~ Unknown\n"
echo "$username" > /home/$username/.UnknownData/username
