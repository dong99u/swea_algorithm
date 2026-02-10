import heapq

numbers = [10, 1, 5, 3, 8, 7, 4]  # 초기 리스트

heapq.heapify(numbers)
print(numbers)

heapq.heappush(numbers, 0)
print(numbers)

print(heapq.heappop(numbers))
print(numbers)

max_heap = []
for num in numbers:
    heapq.heappush(max_heap, -num)
print(max_heap)