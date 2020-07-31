"""
This function that computes the length of the longest path of consecutive integers in a tree. 

A node in the tree has a value and a set of children nodes. A tree has no cycles and each node has exactly one parent. A path where each node has a value 1 greater than its parent is a path of consecutive integers (e.g. 1,2,3 not 1,3,5). 

A few things to clarify:

Integers are all positive
Integers appear only once in the tree
"""

class Tree:
	def __init__(self, value, *children):
		self.value = value
		self.children = children

def recur_path_lengths(tree):
	completed = []
	current = 1
	for child in tree.children:
		path_length = recur_path_lengths(child)
		if tree.value != child.value - 1:
			completed.append(max(path_length))
		else:
			current += path_length[-1]

	if len(completed) == 0 or current >= max(completed):
		return [current]
	else:
		return [max(completed), current]

def longest_path(tree):
  # Implement me
  return max(recur_path_lengths(tree))