# 13:51 ~ X 14:49
import sys
input = sys.stdin.readline

N = int(input())
lines = sorted([list(map(int, input().split())) for _ in range(N)])
dp = [1 for _ in range(N)]

for i in range(N):
    for j in range(i):
        if lines[i][1] > lines[j][1]:
            dp[i] = max(dp[i], dp[j]+1)

print(N - max(dp))

# CONN_CNT = 0
# LAST_NUM = 1

# N = int(input())
# lines = [0] * 501
# max_num = 0
# answer = 0
# for i in range(N):
#     A, B = map(int, input().split())
#     lines[A-1] = B-1
#     max_num = max(max_num, A)

# dp = [[0,0] for _ in range(max_num+1)]
# for i in range(max_num+1):
#     if lines[i] == 0:
#         dp[i][LAST_NUM] = dp[i-1][LAST_NUM]
#         dp[i][CONN_CNT] = dp[i-1][CONN_CNT]
#         continue

#     cross = 0
#     for j in range(i):
#         if dp[j][LAST_NUM] < lines[i]:
#             dp[i][LAST_NUM] = lines[i]
#             dp[i][CONN_CNT] = dp[j][CONN_CNT] + 1
#         else:
#             dp[i][LAST_NUM] = dp[j][LAST_NUM]
#             dp[i][CONN_CNT] = dp[j][CONN_CNT]
#             cross += 1

#     if cross <= 1:
#         dp[i][LAST_NUM] = min(dp[i][LAST_NUM], lines[i])

# answer = dp[-1][0]

# temp = lines.copy()
# for i in range(max_num+1):
#     lines[i] = max_num - temp[max_num-i]

# dp = [[0,0] for _ in range(max_num+1)]
# for i in range(max_num+1):
#     if lines[i] == 0:
#         dp[i][LAST_NUM] = dp[i-1][LAST_NUM]
#         dp[i][CONN_CNT] = dp[i-1][CONN_CNT]
#         continue

#     cross = 0
#     for j in range(i):
#         if dp[j][LAST_NUM] < lines[i]:
#             dp[i][LAST_NUM] = lines[i]
#             dp[i][CONN_CNT] = dp[j][CONN_CNT] + 1
#         else:
#             dp[i][LAST_NUM] = dp[j][LAST_NUM]
#             dp[i][CONN_CNT] = dp[j][CONN_CNT]
#             cross += 1

#     if cross <= 1:
#         dp[i][LAST_NUM] = min(dp[i][LAST_NUM], lines[i])

# answer = max(dp[-1][0], answer)
# print(N - answer)