#!/usr/bin/env python3

from collections import deque
from copy import copy

#   0
# 4 1 5
#   2
#   3

#         T L R B
# route1: 0 1 2 3
# route2: 0 5 2 4
# route3: 1 5 3 4

cube1 = deque(['r', 'b', 'b', 'y', 'g', 'g'])
cube2 = deque(['y', 'r', 'g', 'g', 'b', 'r'])
cube3 = deque(['g', 'r', 'r', 'y', 'b', 'y'])
cube4 = deque(['b', 'y', 'r', 'g', 'y', 'y'])


def orientations(cube):
	ret = []
	route1 = deque([cube[0], cube[1], cube[2], cube[3]])
	route2 = deque([cube[0], cube[5], cube[2], cube[4]])
	route3 = deque([cube[1], cube[5], cube[3], cube[4]])
	routes = [route1, route2, route3]
	for r in routes:
		for i in range(0, 4):
			ret.append(list(r))
			r.rotate()
		r.reverse()
		for i in range(0, 4):
			ret.append(list(r))
			r.rotate()
	return ret

def valid(a, b, c, d):
	for i in range(0, 4):
		if (a[i] == b[i] or
			a[i] == c[i] or
			a[i] == d[i] or
			b[i] == c[i] or
			b[i] == d[i] or
			c[i] == d[i]):
				return False
	return True

orientations1 = orientations(cube1)
orientations2 = orientations(cube2)
orientations3 = orientations(cube3)
orientations4 = orientations(cube4)

for a in orientations1:
	for b in orientations2:
		for c in orientations3:
			for d in orientations4:
				if valid(a, b, c, d):
					solution = [a, b, c, d]
					print (solution)
