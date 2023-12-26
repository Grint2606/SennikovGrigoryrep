class DoubleElement:
    def __init__(self, *lst):
        self.elements = list(lst)
        self.index = 0

    def __next__(self):
        if self.index < len(self.elements):
            pair = (self.elements[self.index], self.elements[self.index + 1] if self.index + 1 < len(self.elements) else None)
            self.index += 2
            return pair
        raise StopIteration

    def __iter__(self):
        return self
