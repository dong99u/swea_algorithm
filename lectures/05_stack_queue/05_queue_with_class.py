class Queue:
    def __init__(self, size=5):
        self.items = [None] * size
        self.size = size
        self.front = -1
        self.rear = -1

    def is_full(self):
        return self.rear == self.size - 1

    def is_empty(self):
        # 값을 삽입할 때 rear 가 1씩 증가
        # 값을 제거할 때 front가 1씩 증가
        # 따라서, 삽입한 만큼 제거했다 -> 비었다.
        # == front 와 rear가 같은 위치에 있다.
        return self.front == self.rear

    def peek(self):
        return self.rear

    def enqueue(self, item):
        if self.is_full():
            raise Exception('Queue가 가득 찼습니다.')

        self.rear += 1
        self.items[self.rear] = item

    def dequeue(self):
        if self.is_empty():
            raise Exception('Queue가 이미 비었습니다.')

        self.front += 1
        deleted_data = self.items[self.front]
        self.items[self.front] = None

        return deleted_data



queue = Queue()

queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)

print(queue.items)

print(queue.dequeue())
print(queue.dequeue())
print(queue.items)
print(queue.peek())

queue.enqueue(4)
queue.enqueue(5)

print(queue.items)
print(queue.is_full())
queue.enqueue(11)