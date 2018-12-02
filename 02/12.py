#!/usr/bin/python3

import itertools
from collections import Counter

strings = []

with open('input', 'r') as f:
	for line in f:
		strings.append(line)

two = 0
three = 0

for string in strings:
	counter = Counter(string)
	for char in range(ord('a'),1+ord('z')):
		n = counter[chr(char)]
		if n == 2:
			two += 1
			break
	for char in range(ord('a'),1+ord('z')):
		n = counter[chr(char)]
		if n == 3:
			three += 1
			break

print("Part 1:", two*three)

for a, b in itertools.combinations(strings, 2):
	diff = 0
	for i in range(0, len(a)):
		if a[i] != b[i]:
			diff += 1
			pos = i
	if diff == 1:
		print("Part 2:", a[:pos] + a[(pos+1):])
