#!/usr/bin/python3

import sys
sys.setrecursionlimit(10000)

max_x = 0
max_y = 0
points = set()

def dist(p1, p2):
	return abs(p2[0]-p1[0]) + abs(p2[1]-p1[1])

def search(p, orig, visited):
	x = p[0]
	y = p[1]
	visited.add(p)
	if x <= 0 or x >= max_x or y <=0 or y >= max_y:
		return -1

	for i in range(-1,2):
		for j in range(-1,2):
			if i == 0 and j == 0 or (x+i, y+j) in visited:
				continue
			shortest_d = 100000000000
			for p in points:
				if orig != p:
					d = dist(p, (x+i,y+j))
					if d < shortest_d:
						shortest_d = d
			if dist(orig, (x+i, y+j)) < shortest_d:
				l = search((x+i, y+j), orig, visited)
				if -1 == l:
					return -1
	return len(visited)


with open('input', 'r') as f:
	for line in f:
		x = int(line.split()[0].strip(','))
		y = int(line.split()[1].strip())
		if x > max_x:
			max_x = x
		if y > max_y:
			max_y = y
		points.add((x,y))


m = 0
for point in points:
	l = search(point, point, set())
	if l > m:
		m = l

print("Part 1:", m)

size = 0
for x in range(0, max_x):
	for y in range(0, max_y):
		totaldist = 0
		for point in points:
			totaldist += dist(point, (x,y))
			if totaldist >= 10000:
				break
		if totaldist < 10000:
			size += 1

print("Part 2:", size)

