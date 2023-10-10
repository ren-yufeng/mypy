#!/usr/bin/env python3

from ipaddress import ip_network, ip_address

import sys

if len(sys.argv) < 3:
    print(f"usage: ${sys.argv[0]} <ip-addr> <cidr>") 
    exit(1)

print(f"Debug: ${sys.argv}")

#ip_addr = sys.argv[1]
#cidr = sys.argv[2]

print(ip_address(sys.argv[1]) in ip_network(sys.argv[2]))
