#!/bin/bash

# Update package lists
apt-get update

# Install packages from packages.txt
xargs -a packages.txt apt-get install -y

# Install Python packages
pip install -r requirements.txt