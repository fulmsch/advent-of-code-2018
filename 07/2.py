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

time = 0

nworkers = 5
workers = []


while nodes != {}:
	candidates = []
	for name,node in nodes.items():
		if node == set():
			candidates.append(name)
	candidates.sort()
	for candidate in candidates:
		if len(workers) < nworkers:
			if any(task["name"] == candidate for task in workers):
				continue
			workers.append({"name":candidate, \
				            "rem":60 + ord(candidate) - ord('A') + 1})
	time += 1
	
	todiscard = set()
	for i in range(0, len(workers)):
		workers[i]["rem"] -= 1
		if workers[i]["rem"] <= 0:
			nodes.pop(workers[i]["name"])
			for k, node in nodes.items():
				node.discard(workers[i]["name"])
			todiscard.add(i)
	for i in todiscard:
		workers.pop(i)

print(time)
