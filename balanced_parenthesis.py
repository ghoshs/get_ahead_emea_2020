"""
Given a string of parentheses, find the size of the longest contiguous substring of balanced parentheses. 
Parentheses are considered balanced when there is a valid closing parenthesis for an opening one.

Example: 

In this string: ())(()), the longest continuous set would be 4 characters long (the last 4 characters of the input).

For )(()))))((((() , the max length would be 4.
()((())(()) = 4
"""

def longest_balanced(string):
	open_paren = {'(': ')'}
	close_paren = {')': '('}
	zero_stack = []
	longest_balanced_length = 0
	for idx, character in enumerate(string):
		if character in open_paren:
			zero_stack.append(idx)
		elif character in close_paren:
			if len(zero_stack) > 0:
				last_zero_idx = zero_stack[-1]
				if close_paren[character] == string[last_zero_idx]:
					balanced = idx - last_zero_idx + 1
					if balanced > longest_balanced_length:
						longest_balanced_length = balanced
					zero_stack.pop()

	return longest_balanced_length