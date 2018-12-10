#!/usr/bin/env pypy3

import re, itertools

def printmsg(pointarray):
	max_x = max([p.x for p in pointarray])
	max_y = max([p.y for p in pointarray])
	min_x = min([p.x for p in pointarray])
	min_y = min([p.y for p in pointarray])

	for y in range(min_y, max_y+1):
		line = ''
		for x in range(min_x, max_x+1):
			if any((x,y) == (p.x, p.y) for p in pointarray):
				line += '#'
			else:
				line += ' '
		print(line)

class Point():
	def __init__(self, line):
		match = re.search(r'position=<\s*(-?\d+),\s*(-?\d+)> velocity=<\s*(-?\d+),\s*(-?\d+)>', line)
		self.x = int(match.group(1))
		self.y = int(match.group(2))
		self.velx = int(match.group(3))
		self.vely = int(match.group(4))
	def update(self):
		self.x += self.velx
		self.y += self.vely
	def undo(self):
		self.x -= self.velx
		self.y -= self.vely
	def dist(self, other):
		return abs(self.x - other.x) + abs(self.y - other.y)

points = []

with open('input', 'r') as f:
	for line in f:
		points.append(Point(line))

n = -1

max_x = max([p.x for p in points])
max_y = max([p.y for p in points])

prevmax_x = 1000000000
prevmax_y = 1000000000

while max_x < prevmax_x and max_y < prevmax_y:
	for p in points:
		p.update()
	n += 1
	prevmax_x = max_x
	prevmax_y = max_y
	max_x = max([p.x for p in points])
	max_y = max([p.y for p in points])

for p in points:
	p.undo()

print("Part 1:\n")
printmsg(points)
print("\nPart 2:", n)
