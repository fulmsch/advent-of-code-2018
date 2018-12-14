#!/usr/bin/env python3

val = [int(x) for x in '554401']

scores = [3, 7]

pos1 = 0
pos2 = 1

while True:
	newscore = int(scores[pos1]) + int(scores[pos2])
	if newscore > 9:
		scores += [1, newscore % 10]
	else:
		scores.append(newscore)
	pos1 = (pos1 + 1 + int(scores[pos1])) % len(scores)
	pos2 = (pos2 + 1 + int(scores[pos2])) % len(scores)
	if scores[-len(val):] == val:
		print(len(scores)-len(val))
		break
	elif scores[-(len(val)+1):-1] == val:
		print(len(scores)-len(val)-1)
		break
