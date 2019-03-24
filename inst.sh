#!/bin/bash

sudo pacman -S python
sudo pacman -S mysql-python
sudo pacman -S python-pip
sudo pip install virtualenv
virtualenv venv
. ./venv/bin/activate
pip install -r requirements.txt
