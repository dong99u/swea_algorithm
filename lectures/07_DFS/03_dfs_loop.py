def dfs(graph, now, visited):
   pass

# 그래프 인접 리스트
graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'E'],
    'D': ['B', 'F'],
    'E': ['B', 'F'],
    'F': ['D', 'E', 'G'],
    'G': ['C']
}

start_vertex = 'A'
visited = set()  # 방문한 정점을 저장할 집합

dfs(graph, start_vertex, visited) 