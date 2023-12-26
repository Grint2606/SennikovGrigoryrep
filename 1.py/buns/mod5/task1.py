class Node:
    def __init__(self, data=None):
        self.data = data
        self.next_node = None

class Stack:
    def __init__(self):
        self.top = None

    def is_empty(self):
        return self.top is None

    def push(self, data):
        new_node = Node(data)
        new_node.next_node = self.top
        self.top = new_node

    def pop(self):
        if self.is_empty():
            return None
        data = self.top.data
        self.top = self.top.next_node
        return data

    def peek(self):
        return None if self.is_empty() else self.top.data
