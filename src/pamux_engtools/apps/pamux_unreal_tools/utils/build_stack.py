class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        result = self.items.append(value)
        return result
    
    def pop(self):
        if len(self.items) == 0:
            return None
        result = self.items.pop()
        return result
    
    def top(self):
        if len(self.items) == 0:
            return None
        return self.items[len(self.items)-1]

BuildStack = Stack()
