class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            return None  # Return None for an empty stack

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return None  # Return None for an empty stack

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)

# Example usage:
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

print("Stack size:", stack.size())
print("Top element:", stack.peek())

while not stack.is_empty():
    item = stack.pop()
    print("Popped:", item)
