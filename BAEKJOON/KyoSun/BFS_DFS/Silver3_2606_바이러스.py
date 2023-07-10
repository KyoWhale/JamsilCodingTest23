# 12:27 ~ 12:42

com_count = int(input())
conn_count = int(input())
connections = [[] * (com_count+1) for _ in range(com_count+1)]

for _ in range(conn_count):
    a, b = map(int, input().split())
    connections[a].append(b)
    connections[b].append(a)

visit = []
q = [1]
while q:
    start = q.pop()
    
    if start in visit:
        continue

    visit.append(start)
    for next in connections[start]:
        q.append(next)
    
print(len(visit) - 1)