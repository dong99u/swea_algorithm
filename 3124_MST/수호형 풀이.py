from collections import defaultdict
import heapq
import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T + 1):
    V, E = map(int, input().split())

    edges = defaultdict(list)
    # 간선 입력 받기
    for _ in range(E):
        n1, n2, w = map(int, input().split())
        # 양방향 간선 구현
        edges[n1].append((w, n1, n2))
        edges[n2].append((w, n2, n1))

    # prim MST
    res = 0
    visited_nodes = set()  # 사이클 구성을 피하기 위해 방문된 노드를 기록합니다.
    searched_edges = []  # 최소 가중치의 간선을 O(1)로 탐색하기 위해 heap으로 활용할 계획입니다.
    cur_node = 1
    # while len(visited_nodes) < V - 1:
    for _ in range(V - 1):
        visited_nodes.add(cur_node)  # 현재 노드를 방문 노드로 기록합니다.

        for w, cn, tn in edges[cur_node]:
            if tn not in visited_nodes:
                # 현재 노드(cn)으로 부터 타겟 노드(tn)까지의 간선을 구성할때
                # 이미 타겟 노드가 방문되어있다면 방문 예약을 하지 않습니다.
                heapq.heappush(searched_edges, (w, cn, tn))

        while True:
            # 최소 가중치의 간선을 탐색합니다.
            # 지금까지 선택할 수 있는 간선들 중에서 가장 낮은 가중치를 갖되,
            # 사이클이 구성되지 않고록 합니다.
            w, cn, tn = heapq.heappop(searched_edges)
            if tn in visited_nodes:
                continue
            else:
                break

        # 최종적으로 선택된 간선을 고려합니다.
        res += w  # 가중치를 더하고,
        cur_node = tn  # 최종 선택된 간선의 타겟 노드에 연결된 또 다른 이웃 간선들을 탐색하도록 합니다.

    print(f"#{tc} {res}")