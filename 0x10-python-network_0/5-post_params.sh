#!/bin/bash
# Write Bash script displays the body of the response
sudo curl -s POST $1 -d "email=test@gmail.com" -d "subject=I will always be here for PLD"
