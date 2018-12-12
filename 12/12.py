#!/usr/bin/env python3

lines = open('input', 'r').readlines()

state = lines[0].strip()

rules = {l[:5]:l[9] for l in lines[1:]}

offset = 0
for i in range(0, 20):
	newstate = state.lstrip('.')
	offset -= len(state)-len(newstate)
	state = '....' + newstate
	offset += 4
	state = state.rstrip('.') + '....'
	newstate = ''
	for x in range(0, len(state) - 4):
		key = state[x:x+5]
		if key in rules:
			newstate += rules[key]
		else:
			newstate += '.'
	state = newstate
	offset -= 2

answer = 0
for i in range(0, len(state)):
	if state[i] == '#':
		answer += i - offset

print('Part 1:', answer)

#After 50000 iterations, the result behaves linearly
print('Part 2:', (50000000000 - 1) * 50 + 1225)
