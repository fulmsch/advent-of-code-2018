#!/usr/bin/env python3

grid = [list(l.strip('\n')) for l in open('input', 'r').readlines()]

carts = [[(' ','') for _ in range(len(grid[0]))] for _ in range(len(grid))]

for y in range(len(grid)):
	for x in range(len(grid[y])):
		c = grid[y][x]
		if c == '>' or c == '<':
			grid[y][x] = '-'
			carts[y][x] = (c, 'left')
		if c == '^' or c == 'v':
			grid[y][x] = '|'
			carts[y][x] = (c, 'left')


while True:
	#break on collision
	#for l in grid: print(''.join(l))
	#for l in carts: print(''.join([c[0] for c in l]))
	newcarts = [[(' ','') for _ in range(len(grid[0]))] for _ in range(len(grid))]
	for y in range(len(carts)):
		for x in range(len(carts[y])):
			c = carts[y][x]
			newc = c
			newx = x
			newy = y
			if c[0] == '<':
				newx -= 1
				track = grid[newy][newx]
				if track == '/':
					newc = ('v', c[1])
				elif track == '\\':
					newc = ('^', c[1])
				elif track == '+':
					if c[1] == 'left':
						newc = ('v', 'straight')
					elif c[1] == 'straight':
						newc = ('<', 'right')
					elif c[1] == 'right':
						newc = ('^', 'left')
					else:
						quit(1)
			elif c[0] == '>':
				newx += 1
				track = grid[newy][newx]
				if track == '/':
					newc = ('^', c[1])
				elif track == '\\':
					newc = ('v', c[1])
				elif track == '+':
					if c[1] == 'left':
						newc = ('^', 'straight')
					elif c[1] == 'straight':
						newc = ('>', 'right')
					elif c[1] == 'right':
						newc = ('v', 'left')
					else:
						quit(3)
			elif c[0] == '^':
				newy -= 1
				track = grid[newy][newx]
				if track == '/':
					newc = ('>', c[1])
				elif track == '\\':
					newc = ('<', c[1])
				elif track == '+':
					if c[1] == 'left':
						newc = ('<', 'straight')
					elif c[1] == 'straight':
						newc = ('^', 'right')
					elif c[1] == 'right':
						newc = ('>', 'left')
					else:
						quit(5)
			elif c[0] == 'v':
				newy += 1
				track = grid[newy][newx]
				if track == '/':
					newc = ('<', c[1])
				elif track == '\\':
					newc = ('>', c[1])
				elif track == '+':
					if c[1] == 'left':
						newc = ('>', 'straight')
					elif c[1] == 'straight':
						newc = ('v', 'right')
					elif c[1] == 'right':
						newc = ('<', 'left')
					else:
						quit(7)
			else:
				continue
			#print(x, y, c)
			if carts[newy][newx] != (' ','') or newcarts[newy][newx] != (' ',''):
				print(str(newx) + ',' + str(newy))
				quit(0)
			newcarts[newy][newx] = newc
			carts[y][x] = (' ','')
	carts = newcarts
