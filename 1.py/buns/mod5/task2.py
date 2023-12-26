class DoubleNode:
    def __init__(self, data=None):
        self.data = data
        self.prev_node = None
        self.next_node = None

class Queue:
    def __init__(self):
        self.front = None
        self.rear = None

    def is_empty(self):
        return self.front is None

    def enqueue(self, data):
        new_node = DoubleNode(data)
        if self.is_empty():
            self.front = self.rear = new_node
        else:
            new_node.prev_node = self.rear
            self.rear.next_node = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            return None
        data = self.front.data
        if self.front == self.rear:
            self.front = self.rear = None
        else:
            self.front = self.front.next_node
            self.front.prev_node = None
        return data
