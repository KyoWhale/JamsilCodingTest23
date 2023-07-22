# 15:26 ~ 15:49
import heapq
import sys
input = sys.stdin.readline

def solution():
    V, E = map(int, input().split())
    K = int(input())
    graph = {}
    for _ in range(E):
        u, v, w = map(int, input().split())
        if u in graph:
            if v in graph[u]:
                graph[u][v] = min(graph[u][v], w)
            else:
                graph[u][v] = w
        else:
            graph[u] = {v:w}

    d = [10e9] * (V+1)
    d[K] = 0
    q = [(d[K], K)]
    while q:
        dist, start = heapq.heappop(q)
        if start not in graph:
            continue
        for next in graph[start]:
            if d[next] > d[start] + graph[start][next]:
                d[next] = d[start] + graph[start][next]
                heapq.heappush(q, (d[next], next))

    for i in d[1:]:
        if i >= 10e9 - 10:
            print("INF")
        else:
            print(i)

solution()