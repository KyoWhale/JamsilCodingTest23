# 14:08 ~ 
import sys
input = sys.stdin.readline

N, M = map(int, input().split())
nodes = [[] for _ in range(N+1)]

for i in range(M):
    A, B = map(int, input().split())
    nodes[A].append(B)
    nodes[B].append(A)

visit = []
count = 0
for i in range(1, N+1):
    if i in visit:
        continue
    visit.append(i)
    count += 1

    q = nodes[i]
    while q:
        start = q.pop()
        if start in visit:
            continue

        visit.append(start)
        for next in nodes[start]:
            if next not in q:
                q.append(next)

print(count)