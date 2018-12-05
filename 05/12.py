#!/usr/bin/python3

def strip(s):
	i = 0
	while i < len(s) - 1:
		if s[i] != s[i+1] and s[i].lower() == s[i+1].lower():
			s = s[:i] + s[i+2:]
			i -= 1
			if i < 0:
				i = 0
		else:
			i += 1
	return len(s)

with open('input', 'r') as f:
	line = f.readline().strip()

shortest = 10000000000000
for c in range(0, 26):
	l = strip(line.replace(chr(c + ord('a')), "").replace(chr(c + ord('A')), ""))
	if l < shortest:
		shortest = l

print('Part 1:', strip(line))
print('Part 2:', shortest)
