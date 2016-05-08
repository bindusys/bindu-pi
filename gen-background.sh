#!/bin/bash  
export DISPLAY=:0.0  

# Create white background image
convert -size 800x480 xc:white base.jpg

# Create IP image
convert base.jpg -pointsize 80 -fill blue -draw "text 0,150 'IPv4: $(ip -4 a s eth0 | grep -Eo 'inet [0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}' | awk '{print $2}')'" -fill black -draw "text -0,250 'Hostname: $(uname -n)'" -pointsize 250  ip.jpg 