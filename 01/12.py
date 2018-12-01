#!/usr/bin/python3

frequency = 0
changes = []
frequencies = set()

with open('input', 'r') as f:
	for line in f:
		changes.append(int(line))
		frequency += int(line)

print('Part 1:', frequency)

frequency = 0
i = 0

while frequency not in frequencies:
	frequencies.add(frequency)
	frequency += changes[i]
	i += 1
	if i >= len(changes):
		i = 0

print('Part 2:', frequency)
