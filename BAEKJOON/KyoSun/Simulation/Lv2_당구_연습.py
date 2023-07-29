# # 16:47 ~ 17:11 X

# def can_vertex(startX, startY, endX, endY):
#     if not (endX == endY and startX == startY):
#         return False
    
#     if endX <= startX:
#         return False
    
#     return True

# def get_vertex(startX, startY, endX, endY):
#     return startX**2 + startY**2 + endX**2 + endY**2

# def can_edge(startX, startY, endX, endY):
#     if abs(startX-endX) % 2 == 0:
#         return True
#     return False

# def get_edge(startX, startY, endX, endY):
#     midX = (startX + endX) // 2
#     return ((startX-midX)**2 + startX**2 + (endX-midX)**2 + endY**2)

# def rotate(m, n, startX, startY, endX, endY, direction):
#     if direction == 0:
#         return startX, startY, endX, endY
#     elif direction == 1:
#         return
#     elif direction == 2:
#         return
#     else:
#         return

# def solution(m, n, startX, startY, balls):
#     answer = []

#     for ballX, ballY in balls:
#         minimal = 10e9
#         for d in range(4):
#             nX, nY, eX, eY = rotate(m, n, startX, startY, ballX, ballY, d)
#             if can_vertex(nX, nY, eX, eY):
#                 minimal = min(minimal, get_vertex(nX, nY, eX, eY))


#     return answer

def solution(m, n, startX, startY, balls):
    answer = []
    for endX, endY in balls:
        temp = []

        if not (startX == endX and startY < endY):
            temp.append((startX - endX)**2 + (n-startY + n-endY)**2)
        if not (startX == endX and startY > endY):
            temp.append((startX - endX)**2 + (startY + endY)**2)
        if not (startY == endY and startX > endX):
            temp.append((startX + endX)**2 + (startY - endY)**2)
        if not (startY == endY and startX < endX):
            temp.append((m-startX + m-endX)**2 + (startY - endY)**2)

        answer.append(min(temp))
    return answer

print(solution(10, 10, 3, 7, [[7, 7], [2, 7], [7, 3]]))