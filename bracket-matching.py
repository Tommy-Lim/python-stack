class Stack:
    def __init__(self):
        self.data = []

    def push(self, value):
        self.data.append(value)

    def pop(self):
        if len(self.data)>0:
            return self.data.pop()
        return None

    def size(self):
        return len(self.data)

    def __len__(self):
        return self.size()

ss = Stack()

ss.push(42)
ss.push(10)
ss.push(9)
print(len(ss))
