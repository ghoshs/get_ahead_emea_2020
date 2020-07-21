from balanced_parenthesis import longest_balanced
from evaluate import evaluate

def visibletc1():
	assert longest_balanced('') == 0

def visibletc2():
	assert longest_balanced('(()())') == 6

def hiddentc1():
	assert longest_balanced('()(') == 2

def hiddentc2():
	assert longest_balanced('())(())') == 4

def hiddentc3():
	assert longest_balanced('(())') == 4

def hiddentc4():
	assert longest_balanced('((') == 0

def hiddentc5():
	assert longest_balanced('())') == 2

def hiddentc6():
	assert longest_balanced('(') == 0

def hiddentc7():
	assert longest_balanced(')') == 0

def hiddentc8():
	assert longest_balanced(')(()))))(((()') == 4

def hiddentc9():
	assert longest_balanced('()((())(())') == 4


def evaluate_balancedParenthesis():
	evaluate([visibletc1, visibletc2, hiddentc1, hiddentc2, hiddentc3, hiddentc4, hiddentc5, hiddentc6, hiddentc7, hiddentc8, hiddentc9])