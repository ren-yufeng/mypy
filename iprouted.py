#!/usr/bin/env python3

from cidr_trie import PatriciaTrie
import sys

if len(sys.argv) < 3:
    print(f"Usage: sys.argv[0]  <ip-address>  <cidr-list-file-name>")
    exit(1)

f = open(sys.argv[2], 'r')

prefix_trie = PatriciaTrie()

line = f.readline()
while line:
    print(line)
    prefix_trie.insert(line.removesuffix("\n"), "destination-cidr")
    line = f.readline()

f.close()

print(prefix_trie)

print("\n\n** Destinations: ", prefix_trie.find_all(sys.argv[1]))
