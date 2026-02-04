class Stack:
    def __init__(self, size=10):
        self.size = size
        self.items = [None] * size
        self.top = -1 # stack 이 비어있음

    def is_full(self):
        return self.top == self.size - 1

    def is_empty(self):
        return self.top == -1

    def push(self, data):
        if self.is_full():
            raise Exception('Stack이 가득 찼습니다.')

        self.top += 1
        self.items[self.top] = data

    def pop(self):
        if self.is_empty():
            raise Exception('Stack이 비어있습니다.')

        pop = self.items[self.top]
        self.items[self.top] = None
        self.top -= 1

        return pop

    def peek(self):
        if self.is_empty():
            raise Exception('Stack이 비어있습니다.')
        return self.top



stack = Stack()

stack.push(1)
stack.push(2)
stack.push(3)
print(stack.items)

print(stack.pop())
print(stack.pop())
print(stack.peek())
print(stack.is_empty())
print(stack.pop())
print(stack.pop())
