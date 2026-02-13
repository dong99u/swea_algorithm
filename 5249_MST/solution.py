import sys
sys.stdin = open('input.txt')

def find(x):
     if parent[x] != x:
          parent[x] = find(parent[x])
     return parent[x]

def union(x, y):
     x = find(x)
     y = find(y)

     if x != y:
          parent[y] = x


t = int(input())

for test_case in range(1, t + 1):

     n, m = map(int, input().split())
     edges = []

     parent = [i for i in range(n + 1)]
     for _ in range(m):
          u, v, w = map(int, input().split())
          edges.append((u, v, w))

     edges.sort(key=lambda x: x[2])

     answer = 0
     for u, v, w in edges:
          if find(u) != find(v):
               answer += w
               union(u, v)


     print(f'#{test_case} {answer}')