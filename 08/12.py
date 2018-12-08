#!/usr/bin/env python3

with open('input', 'r') as f:
	numbers = [int(x) for x in f.readline().strip().split(' ')]


def build_tree():
	node = {'children': [], 'metadata': []}
	children = numbers.pop(0)
	metadata = numbers.pop(0)
	for i in range(0, children):
		node['children'].append(build_tree())
	for i in range(0, metadata):
		node['metadata'].append(numbers.pop(0))
	return node

def part1(node):
	s = 0
	for child in node['children']:
		s += part1(child)
	for metadata in node['metadata']:
		s += metadata
	return s

def part2(node):
	val = 0
	if node['children'] == []:
		val = sum(node['metadata'])
	else:
		for n in node['metadata']:
			if n <= len(node['children']) and n > 0:
				val += part2(node['children'][n-1])
	return val

tree = build_tree()

print("Part 1:", part1(tree))
print("Part 2:", part2(tree))
