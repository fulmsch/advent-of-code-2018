#!/usr/bin/env python3

recipes = 554401

scores = [3, 7]

pos1 = 0
pos2 = 1

while len(scores) < recipes + 10:
	newscore = scores[pos1] + scores[pos2]
	if newscore > 9:
		scores += [1, newscore % 10]
	else:
		scores.append(newscore)
	pos1 = (pos1 + 1 + scores[pos1]) % len(scores)
	pos2 = (pos2 + 1 + scores[pos2]) % len(scores)

print(''.join(str(c) for c in scores[-10:]))
