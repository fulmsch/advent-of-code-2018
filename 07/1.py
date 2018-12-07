#!/usr/bin/env python3

import re

nodes = {}

def addnode(parent, child):
	try:
		nodes[parent]
	except KeyError:
		nodes[parent] = set()

	try:
		nodes[child]
	except KeyError:
		nodes[child] = set()
	nodes[child].add(parent)

with open('input', 'r') as f:
	for line in f:
		match = re.search(r'^.*\s([A-Z]).*\s([A-Z])', line)
		addnode(match.group(1), match.group(2))

output = ""

while nodes != {}:
	candidates = []
	for name,node in nodes.items():
		if node == set():
			candidates.append(name)

	candidates.sort()
	name = candidates[0]
	output += name
	nodes.pop(name)
	for k, node in nodes.items():
		node.discard(name)

print(output)
