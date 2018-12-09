#!/usr/bin/env python3

class Marble():
	def __init__(self, _value, _prev, _next):
		self.value = _value
		self.prev = _prev
		self.next = _next

def dothething(players, lastmarble):
	scores = [0 for x in range(players)]

	player = 0
	index = Marble(0, None, None)
	index.prev = index
	index.next = index
	for curmarble in range(1, lastmarble + 1):
		if curmarble % 23 == 0:
			scores[player] += curmarble
			toremove = index.prev.prev.prev.prev.prev.prev.prev
			toremove.prev.next = toremove.next
			toremove.next.prev = toremove.prev
			scores[player] += toremove.value
			index = toremove.next
		else:
			new = Marble(curmarble, index.next, index.next.next)
			index.next.next.prev = new
			index.next.next = new
			index = new

		player = (player + 1) % players
	return max(scores)

players = 452
lastmarble = 71250

print("Part 1:", dothething(players, lastmarble))
print("Part 2:", dothething(players, lastmarble * 100))
