# 14:17 ~ 14:47

import sys
input = sys.stdin.readline

def solution():
    N, M, K, X = map(int, input().split())
    graph = {}
    for _ in range(M):
        start, end = map(int, input().split())
        if start in graph:
            graph[start].append(end)
        else:
            graph[start] = [end]

    d = [10e9] * (N+1)
    d[X] = 0
    q = [X]
    answer = set()
    while q:
        start = q.pop(0)
        if start not in graph:
            continue
        if d[start] > K:
            continue

        for next in graph[start]:
            if d[next] > d[start] + 1:
                q.append(next)
                d[next] = d[start] + 1
                if d[next] == K:
                    answer.add(next)

    if len(answer) == 0:
        print(-1)
        return

    for i in sorted(list(answer)):
        print(i)

solution()