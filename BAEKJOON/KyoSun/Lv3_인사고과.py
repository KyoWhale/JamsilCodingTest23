def solution(scores):
    wanho = scores[0]
    wanho_score = sum(wanho)

    scores.sort(key=lambda x: (-x[0], x[1]))

    answer = 1
    low = 0 # [높은순, 낮은순]에서 직전의 0인덱스보다 현재의 1인덱스가 커야함
    for a, b in scores:
        if wanho[0] < a and wanho[1] < b:
            return -1
        
        if wanho_score < a+b and low <= b: # a는 무조건 작으니까 b라도 커야한다
            answer += 1
            low = b

    return answer

# # 18:41 ~ 18:47 X

# import heapq

# def solution(scores):
#     loser = []
#     total = []
#     for i in range(0, len(scores)):
#         for j in range(i+1, len(scores)):
#             if scores[i][0] < scores[j][0] and scores[i][1] < scores[j][1]:
#                 loser.append(i)
#                 break

#         score = scores[i][0] + scores[i][1]
#         heapq.heappush(total, (-score, i))

#     if 0 in loser:
#         return -1
    
#     answer = 0
#     while total:
#         answer += 1
#         _, i = heapq.heappop(total)
#         if i == 0:
#             return answer

# # 18:13 ~ 18:41 X

# def solution(scores):
#     loser = []
#     total = {}
#     for i in range(0, len(scores)):
#         for j in range(i+1, len(scores)):
#             if scores[i][0] < scores[j][0] and scores[i][1] < scores[j][1]:
#                 loser.append(i)
#                 break

#         score = scores[i][0] + scores[i][1]
#         if score in total:
#             total[score].append(i)
#         else:
#             total[score] = [i]

#     if 0 in loser:
#         return -1

#     wanho = sum(scores[0])
#     answer = 1
#     for big in sorted([i for i in total.items()], reverse=True):
#         if big[0] > wanho:
#             answer += len(big[1])
#         else:
#             break
#     return answer

print(solution([[2,2],[1,4],[3,2],[3,2],[2,1]]))