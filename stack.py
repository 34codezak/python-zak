# Define a base class
class Stack:
	def __init__(self):
		self.items = []

	# Operation to add an element to a stack
	def push(self, item):
		self.items.append(item)

	# Operation to remove the last element of our stack
	def pop(self):
		if not self.is_empty():
			return self.items.pop()
		return None

	# The peek operation - returns the top element without removing it
	def peek(self):
		if not self.is_empty():
			return self.items[-1]

		return None

	# Helper method to check if stack is empty
	def is_empty(self):
		return len(self.items) == 0

stack = Stack()
stack.push(5)
stack.push(8)
stack.push(11)
stack.push(230)

print(stack.peek())
stack.pop()

print(stack.items)
