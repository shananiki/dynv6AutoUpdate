#!/bin/bash

# Install Python 3
if ! command -v python3 &> /dev/null; then
    sudo apt-get update
    sudo apt-get install -y python3
fi

# Install pip3
if ! command -v pip3 &> /dev/null; then
    sudo apt-get update
    sudo apt-get install -y python3-pip
fi

# Install requests using pip3
sudo pip3 install requests

echo "Installation complete!"
