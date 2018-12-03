#!/usr/bin/env python3

import re

used = set()
multiples = set()
squares = [[0] * 10000 for i in range(10000)]

with open('input', 'r') as f:
	for line in f:
		match = re.search(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', line)
		if match == None:
			continue
		xoffs = int(match.group(2))
		yoffs = int(match.group(3))
		width = int(match.group(4))
		height = int(match.group(5))
		for x in range(xoffs, xoffs+width):
			for y in range(yoffs, yoffs+height):
				squares[x][y] += 1
				if (x,y) in used:
					multiples.add((x,y))
				else:
					used.add((x,y))
	print("Part 1:", len(multiples))

	f.seek(0)
	for line in f:
		match = re.search(r'#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', line)
		if match == None:
			continue
		claim = int(match.group(1))
		xoffs = int(match.group(2))
		yoffs = int(match.group(3))
		width = int(match.group(4))
		height = int(match.group(5))
#		print(xoffs, yoffs, width, height)
		overlapping = False
		for x in range(xoffs, xoffs+width):
			for y in range(yoffs, yoffs+height):
				if squares[x][y] > 1:
					overlapping = True
		if overlapping == False:
			print("Part 2:", claim)
