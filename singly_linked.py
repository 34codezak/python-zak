# linked list implementation in Python
# operation; insert, delete, display, length, search

# 1. insertion at start
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None