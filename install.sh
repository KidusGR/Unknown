#!/usr/bin/env bash
#Install Unknown

sudo pip3 install -r ./requirments.txt
sudo mkdir -p ./Data/ && sudo touch ./Data/words && sudo chmod u+x ./Unknown.py && sudo cp Unknown.py /usr/local/bin/Unknown && echo -e "\n\nNow just run\n$~ Unknown\n"

