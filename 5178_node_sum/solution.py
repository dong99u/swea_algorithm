import sys
sys.stdin = open('input.txt')

t = int(input())

def dfs(v):
    # 범위 밖 노드라면
    if v >= n:
        return 0

    # 이미 값이 있으면 (리프 노드) 그대로 반환
    if tree[v] is not None:
        return tree[v]

    # 내부 노드: 자식들의 합을 계산하여 저장
    tree[v] = dfs(2*v + 1) + dfs(2*v + 2)
    return tree[v]


for tc in range(1, t + 1):
    n, m, l = map(int, input().split())

    tree = [None] * n
    for _ in range(m):
        v, w = map(int, input().split())
        v -= 1
        tree[v] = w

    dfs(0)

    print(f'#{tc} {tree[l - 1]}')