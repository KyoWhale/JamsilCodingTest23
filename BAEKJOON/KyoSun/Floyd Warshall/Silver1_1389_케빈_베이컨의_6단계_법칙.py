# 11:20 ~ 12:14 X O

MAX = 10e9

def solution():
    N, M = map(int, input().split())
    
    graph = [[MAX] * (N+1) for _ in range(N+1)]
    for _ in range(M):
        A, B = map(int, input().split())
        graph[A][B] = 1
        graph[B][A] = 1

    for k in range(1, N+1):
        for i in range(1, N+1):
            for j in range(1, N+1):
                if graph[i][k] >= MAX-10 and graph[k][j] >= MAX-10:
                    continue

                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
                graph[j][i] = graph[i][j]

    answer = (10e9, 0)
    for i in range(1, N+1):
        if sum(graph[i][1:]) < answer[0]:
            answer = (sum(graph[i][1:]), i)
        
    print(answer[1])

solution()

# 5 6
# 1 3
# 1 3
# 1 4
# 4 5
# 4 3
# 3 2