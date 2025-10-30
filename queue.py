class Queue:
	def __init__(self):
		self.queue = []

	def enqueue(self, item):
		self.queue.append(item)

	def dequeue(self):
		if not self.is_empty():
			return self.queue.pop()
		return "Queue is empty"

	def peek(self):
		if not self.is_empty():
			return self.queue[0]
		return "Queue is empty"

	# Method to check is the queue is empty
	def is_empty(self):
		return len(self.queue) == 0

# Use cases
q = Queue()
q.enqueue(4)
q.enqueue(8)
q.enqueue(20)
print(q.dequeue()) # Output: 20
print(q.peek()) # Output: 4
