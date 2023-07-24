# 14:48 ~ 15:06

def solution():
    N = int(input())
    graph = [0] * N
    for i in range(N):
        graph[i] = list(map(int, input().split()))

    for k in range(N):
        for i in range(N):
            for j in range(N):
                if graph[i][k] == 1 and graph[k][j] == 1:
                    graph[i][j] = 1

    for col in graph:
        for i in col:
            if i == 1:
                print("1 ", end="")
            else:
                print("0 ", end="")
        print()

solution()