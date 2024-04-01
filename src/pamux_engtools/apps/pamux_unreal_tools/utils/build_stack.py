class Stack:
    def __init__(self):
        self.items = []

    def push(self, value):
        print(f"prepush {len(self.items)}")
        result = self.items.append(value)
        print(f"postpush {len(self.items)}")
        return result
    
    def pop(self):
        print(f"prepop {len(self.items)}")
        if len(self.items) == 0:
            print(f"postpop {len(self.items)}")
            return None
        result = self.items.pop()
        print(f"postpop {len(self.items)}")
        return result
    
    def top(self):
        print(f"pretop {len(self.items)}")
        if len(self.items) == 0:
            return None
        return self.items[len(self.items)-1]

print("BuildStack")
BuildStack = Stack()


class NodePos:
    DeltaX = 400
    DeltaY = 300
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def goto_inputs(self):
        self.x = 0
        self.y = 0

    def goto_process(self):
        self.x = 3 * NodePos.DeltaX
        self.y = 0

    def goto_outputs(self):
        self.x = 6 * NodePos.DeltaX
        self.y = 0

    def dump(self, s):
        print(f"{s}: {self.x} {self.y}")

CurrentNodePos = NodePos(0, 0)
