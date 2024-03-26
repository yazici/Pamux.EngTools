class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        return self.items.append(value)
    
    def pop(self):
        if len(self.items) == 0:
            return None
        return self.items.pop()
    
    def top(self):
        if len(self.items) == 0:
            return None
        return self.items[len(self.items)-1]


BuildStack = Stack()


class NodePos:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

CurrentNodePos = NodePos(0, 0)
