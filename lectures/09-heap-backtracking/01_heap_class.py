# class MinHeap:
#     def __init__(self):
#         self.heap = []  # 힙을 저장할 빈 리스트 초기화
#         self.length = 0  # 힙의 길이 초기화
#
#     # 힙에 새로운 요소를 추가
#     def heappush(self, item):
#         self.heap.append(item)  # 새로운 요소를 리스트의 끝에 추가
#         self.length += 1  # 힙의 길이 증가
#
#     # 힙에서 최소 요소를 제거하고 반환
#     def heappop(self):
#         if self.length == 0:
#             raise IndexError("힙이 비었습니다.")  # 힙이 비어 있는 경우 예외 발생
#         if self.length == 1:
#             self.length -= 1
#             return self.heap.pop()  # 힙에 요소가 하나만 있는 경우 그 요소를 반환
#
#     # 주어진 리스트을 힙으로 변환
#     def heapify(self, array):
#         self.heap = array[:]  # 리스트의 복사본을 힙으로 사용
#         self.length = len(array)
#
#     # 삽입 후 힙 속성을 유지하기 위해 사용되는 보조 메서드
#     def _siftup(self, idx):
#         pass
#
#     # 삭제 후 힙 속성을 유지하기 위해 사용되는 보조 메서드
#     def _siftdown(self, idx):
#         pass
#
#     def __str__(self):
#         return str(self.heap)  # 힙의 문자열 표현 반환

class MinHeap:
    def __init__(self, item=[]):
        self.item = item
        self.make_heap()

    def heapify_down(self, k):
        n = len(self.item)

        while 2 * k + 1 < n:
            L, R = 2 * k + 1, 2 * k + 2

            if self.item[L] < self.item[k]:
                m = L
            else:
                m = R

            if R < n and self.item[R] < self.item[m]:
                m = R

            if m != k:
                self.item[k], self.item[m] = self.item[m], self.item[k]
                k = m
            else:
                break

    def heapify_up(self, k):
        while k > 0 and self.item[(k - 1) // 2] > self.item[k]:
            self.item[k], self.item[(k - 1) // 2] = self.item[(k - 1) // 2], self.item[k]
            k = (k - 1) // 2

    def insert(self, key):
        self.item.append(key)
        self.heapify_up(len(self.item) - 1)

    def pop(self):
        if len(self.item) == 0: return None
        key = self.item[0]

        self.item[0], self.item[len(self.item) - 1] = self.item[len(self.item) - 1]
        self.item.pop()
        self.heapify_down(0)

        return key

    def make_heap(self):
        n = len(self.item)

        for k in range(n - 1, -1, -1):
            self.heapify_down(k)

min_heap = MinHeap()
min_heap.heappush(3)
min_heap.heappush(1)
min_heap.heappush(2)

print(min_heap)  # [1, 3, 2]
print(min_heap.heappop())  # 1
print(min_heap)  # [2, 3]

min_heap.heapify([5, 4, 3, 2, 1])
print(min_heap)  # [1, 2, 3, 5, 4]
print(min_heap.heappop())  # 1
print(min_heap)  # [2, 4, 3, 5] 
print(min_heap.heappop())  # 2
print(min_heap)  # [3, 4, 5]