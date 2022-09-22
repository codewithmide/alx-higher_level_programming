#!/bin/bash
# Write a Bash script that takes The size must be displayed in bytes
sudo curl -i -s $1 | grep "Content-Length" | cut -d ' ' -f2
