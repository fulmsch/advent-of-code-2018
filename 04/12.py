#!/usr/bin/env python3

import re

class Log_entry():
	def __init__(self, line):
		match = re.search(r'\[1518-(\d\d)-(\d\d) (\d\d):(\d\d)\] (.*)', line)
		if match == None:
			return
		entry = match.group(5).split()
		if entry[0] == "Guard":
			self.type = int(entry[1].strip('#'))
		else:
			self.type = entry[0]
		self.minute = int(match.group(4))
		self.timestamp = int(match.group(4)) + \
		                 60*int(match.group(3)) + \
		                 60*24*int(match.group(2)) + \
		                 60*24*31*int(match.group(1))

logs = []
guards = {}

with open('input', 'r') as f:
	for line in f:
		logs.append(Log_entry(line))

logs.sort(key=lambda x: x.timestamp, reverse=False)

for log in logs:
	if log.type == "falls":
		start_minute = log.minute
	elif log.type == "wakes":
		stop_minute = log.minute
		guards[cur_guard]['total'] += stop_minute - start_minute
		for i in range(start_minute, stop_minute):
			guards[cur_guard]['minutes'][i] += 1
	else:
		cur_guard = log.type
		try:
			guards[cur_guard]
		except KeyError:
			guards[cur_guard] = {'total': 0, 'minutes': []}
			for i in range(0,60):
				guards[cur_guard]['minutes'].insert(i,0)

max_minutes = 0
for k,v in guards.items():
	if v['total'] > max_minutes:
		max_minutes = v['total']
		max_guard = k

max_times = 0
for i in range(0,60):
	times = guards[max_guard]['minutes'][i]
	if times > max_times:
		max_times = times
		max_minute = i

print("Part 1:", max_guard * max_minute)

max_times = 0
for k,v in guards.items():
	times = max(v['minutes'])
	if  times > max_times:
		max_times = times
		max_guard = k
		max_minute = v['minutes'].index(times)

print("Part 2:", max_guard, max_minute, max_guard * max_minute)
