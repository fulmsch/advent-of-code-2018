#!/usr/bin/env python3

import math

serial = 7689

def cell(x, y):
	rack_id = x + 10
	pwr = (rack_id * y + serial) * rack_id
	pwr = math.floor(pwr / 100) % 10
	return pwr - 5

def line (y):
	return [cell(x, y) for x in range(1, 301)]

def square(x, y, size):
	val = 0
	for xoffs in range(0, size):
		for yoffs in range(0, size):
			val += lines[y + yoffs - 1][x + xoffs - 1]
	return val

lines = [line(y) for y in range(1, 301)]

maxval = -100000000
for y in range(1, 299):
	for x in range(1, 299):
		val = square(x, y, 3)
		if val > maxval:
			maxval = val
			maxsquare = (x, y)

print('Part 1: ' + str(maxsquare[0]) + ',' + str(maxsquare[1]))

maxval = -100000000
for size in range(1, 20):
	for y in range(1, 302 - size):
		for x in range(1, 302 - size):
			val = square(x, y, size)
			if val > maxval:
				maxval = val
				maxsquare = (x, y, size)

print('Part 2: ', str(maxsquare[0]) + ',' + str(maxsquare[1]) + ',' + str(maxsquare[2]))
