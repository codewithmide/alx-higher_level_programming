#!/bin/bash
# Write Bash script x header variable X-School must be sent with the value 98
sudo curl -s -X GET $1 -H "X-School-User-Id: 98"
