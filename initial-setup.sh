#!/bin/sh

echo "############################"
echo "bindu-rpi - Initial Setup"
echo "############################"
echo ""
echo "=== Install python headers ==="
sudo apt-get install libpython-all-dev

echo ""
echo "=== Install Fabric ==="
sudo pip install -I fabric

echo ""
echo "Bindu done.. now run `fab -l` "



    
