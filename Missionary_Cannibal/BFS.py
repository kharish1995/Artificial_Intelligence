import numpy as np
import math
class State():
	def __init__(self, cl, ml, boat, cr, mr):
		self.cl = cl
		self.ml = ml
		self.boat = boat
		self.cr = cr
		self.mr = mr
		self.p = None
	def is_goal(self):
		if self.cl == 0 and self.ml == 0:
			return True
		else:
			return False
	def is_valid(self):
		if self.ml >= 0 and self.mr >= 0 \
                   and self.cl >= 0 and self.cr >= 0 \
                   and (self.ml == 0 or self.ml >= self.cl) \
                   and (self.mr == 0 or self.mr >= self.cr):
			return True
		else:
			return False
	def _eq_(self, other):
		return self.cl == other.cl and self.ml == other.ml \
                   and self.boat == other.boat and self.cr == other.cr \
                   and self.mr == other.mr

	def _hash_(self):
		return hash((self.cl, self.ml, self.boat, self.cr, self.mr))

def successors(pre):
	c = [];
	if pre.boat == 'l':
		post = State(pre.cl, pre.ml - 2, 'r',
                                  pre.cr, pre.mr + 2)
		if post.is_valid():
			post.p = pre
			c.append(post)
		post = State(pre.cl - 2, pre.ml, 'r', pre.cr + 2, pre.mr)
		if post.is_valid():
			post.p = pre
			c.append(post)
		post = State(pre.cl - 1, pre.ml - 1, 'r', pre.cr + 1, pre.mr + 1)
		if post.is_valid():
			post.p = pre
			c.append(post)
		post = State(pre.cl, pre.ml - 1, 'r', pre.cr, pre.mr + 1)
		if post.is_valid():
			post.p = pre
			c.append(post)
		post = State(pre.cl - 1, pre.ml, 'r', pre.cr + 1, pre.mr)
		if post.is_valid():
			post.p = pre
			c.append(post)
	else:
		post = State(pre.cl, pre.ml + 2, 'l', pre.cr, pre.mr - 2)
		if post.is_valid():
			post.p = pre
			c.append(post)
		post = State(pre.cl + 2, pre.ml, 'l', pre.cr - 2, pre.mr)
		if post.is_valid():
			post.p = pre
			c.append(post)
		post = State(pre.cl + 1, pre.ml + 1, 'l', pre.cr - 1, pre.mr - 1)
		if post.is_valid():
			post.p = pre
			c.append(post)
		post = State(pre.cl, pre.ml + 1, 'l', pre.cr, pre.mr - 1)
		if post.is_valid():
			post.p = pre
			c.append(post)
		post = State(pre.cl + 1, pre.ml, 'l', pre.cr - 1, pre.mr)
		if post.is_valid():
			post.p = pre
			c.append(post)
	return c
def bfs():
	initial_state = State(3,3,'l',0,0)
	if initial_state.is_goal():
		return initial_state
	frontier = list()
	explored = set()
	frontier.append(initial_state)
	while frontier:
		state = frontier.pop(0)
		if state.is_goal():
			return state
		explored.add(state)
		c = successors(state)
		for child in c:
			if (child not in explored) or (child not in frontier):
				frontier.append(child)
	return None
def print_solution(solution):
		path = []
		path.append(solution)
		p = solution.p
		while p:
			path.append(p)
			p = p.p
		for t in range(len(path)):
			state = path[len(path) - t - 1]
			print "(" + str(state.cl) + "," + str(state.ml) + "," + state.boat + "," + str(state.cr) + "," + str(state.mr) + ")"

def main():
	solution = bfs()
	print "(cl,ml,boat,cr,mr)"
	print_solution(solution)
if __name__ == "__main__":
    main()
