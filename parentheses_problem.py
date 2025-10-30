# Method to solove the parentheses problem
def is_balanced(expression):
	stack = []
	pairs = {')': '(', ']': '[', '}': '{'}

	for char in expression:
		if char in pairs.values(): # Opening symbols
			stack.append(char)
		elif char in pairs.keys(): # Closing symbols
			if not stack or stack[-1] != pairs[char]:
				return False
			stack.pop()

	return len(stack) == 0

# Test cases
print(is_balanced("({[]})")) # Output: True
print(is_balanced("{[}]")) # Output: False
print(is_balanced("")) # Output: True - no parentheses to march
