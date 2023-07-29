# 15:53 ~ 

def solution(sequence, k):
    answer = [0, 10e7]
    length = len(sequence)
    
    start, end = 0, -1
    sum = 0
    
    while True:
        if sum < k:
            end += 1
            if end >= length:
                break
            sum += sequence[end]
        else:
            sum -= sequence[start]
            if start >= length:
                break
            start += 1

        if sum == k and answer[1] - answer[0] > end - start:
            answer[0], answer[1] = start, end
    
    return answer

print(solution([1,2,3,4,5], 7))
print(solution([1, 1, 1, 2, 3, 4, 5], 5))
print(solution([2, 2, 2, 2, 2], 6))