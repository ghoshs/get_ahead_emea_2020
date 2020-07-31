from evaluate import evaluate
from longest_tree_path import Tree, longest_path

# left example
def visibletc1():
	tree = Tree(1, Tree(2, Tree(4)), Tree(3))
	assert longest_path(tree) == 2

# right example
def visibletc2(): 
	tree = Tree(5, Tree(6), Tree(7, Tree(8, Tree(9, Tree(15), Tree(10))), Tree(12)))
	assert longest_path(tree) == 4 

# single element tree
def hiddentc1():
	tree = Tree(1)
	assert longest_path(tree) == 1

# no consecutive integers
def hiddentc2():
	tree = Tree(5, Tree(7), Tree(8, Tree(10, Tree(13, Tree(15), Tree(17))), Tree(12)))
	assert longest_path(tree) == 1 

# one level deep
def hiddentc3():
	tree = Tree(3, Tree(4))
	assert longest_path(tree) == 2

# no siblings
def hiddentc4():
	tree = Tree(3, Tree(5, Tree(6)))
	assert longest_path(tree) == 2

# begin path in root end in leaf
def hiddentc5():
	tree = Tree(3, Tree(9), Tree(4, Tree(5, Tree(6), Tree(8))))
	assert longest_path(tree) == 4

# begin in root don't end in leaf
def hiddentc6():
	tree = Tree(3, Tree(9), Tree(4, Tree(5, Tree(6, Tree(11)), Tree(8))))
	assert longest_path(tree) == 4	

# don't begin in root, don't end in leaf
def hiddentc7():
	tree = Tree(13,
	            Tree(32,
	                 Tree(40),
	                 Tree(26)),
	            Tree(27,
	                 Tree(20,
	                      Tree(6)),
	                 Tree(16),
	                 Tree(21,
	                      Tree(22,
	                           Tree(23,
	                                Tree(3,
	                                     Tree(31)),
	                                Tree(15,
	                                     Tree(11)),
	                                Tree(8))),
	                      Tree(33,
	                           Tree(19),
	                           Tree(2,
	                                Tree(18),
	                                Tree(24)),
	                           Tree(34))),
	                 Tree(1,
	                      Tree(37),
	                      Tree(30))),
	            Tree(7),
	            Tree(5,
	                 Tree(4),
	                 Tree(38)))
	assert(longest_path(tree) == 3)

# don't begin in root, end in leaf
def hiddentc8():
	tree = Tree(32,
	            Tree(34,
	                 Tree(12),
	                 Tree(35,
	                      Tree(21),
	                      Tree(40),
	                      Tree(1)),
	                 Tree(4,
	                      Tree(9,
	                           Tree(20),
	                           Tree(27),
	                           Tree(2),
	                           Tree(39)),
	                      Tree(11,
	                           Tree(25),
	                           Tree(30)),
	                      Tree(5,
	                           Tree(19),
	                           Tree(6,
	                                Tree(7,
	                                     Tree(8),
	                                     Tree(33),
	                                     Tree(17),
	                                     Tree(16)))),
	                      Tree(3)),
	                 Tree(36,
	                      Tree(24))),
	            Tree(28,
	                 Tree(23),
	                 Tree(15),
	                 Tree(10)))
	assert(longest_path(tree) == 5)

# very wide tree
def hiddentc9():
	tree = Tree(3, Tree(5), Tree(6), Tree(7), Tree(8), Tree(9), Tree(10), Tree(11), Tree(12), Tree(13))
	assert longest_path(tree) == 1


# very deep tree
def hiddentc10():
	tree = Tree(3, Tree(5, Tree(6, Tree(7, Tree(8, Tree(9, Tree(10, Tree(11, Tree(12, Tree(13))))))))))
	assert longest_path(tree) == 9

def hiddentc11():
	tree = Tree(1,
				Tree(8),
				Tree(2, 
					Tree(4, 
						 Tree(5,
						 	  Tree(6))),
					Tree(3)))
	assert longest_path(tree) == 3

def evaluate_longestPath():
	evaluate([visibletc1, visibletc2, hiddentc1, hiddentc2, hiddentc3, hiddentc4, hiddentc5, hiddentc6, hiddentc7, 
		hiddentc8, hiddentc9, hiddentc10, hiddentc11])