from balanced_parenthesis import longest_balanced
from evaluate import evaluate

def testcase1():
	assert longest_balanced('(()())') == 6

def testcase2():
	assert longest_balanced(')(())(())(()') == 8

if __name__ == '__main__':
	evaluate([testcase1, testcase2])