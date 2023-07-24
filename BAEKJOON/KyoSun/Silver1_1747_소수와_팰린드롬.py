# 12:15 ~ 13:10

import math

def isPrime(N):
    if N == 1:
        return False
    for i in range(2, int(math.sqrt(N))+1):
        if N % i == 0:
            return False
    return True

def isPalindrome(N):
    if str(N) == str(N)[::-1]:
        return True
    return False

N = int(input())

while True:
    if isPalindrome(N) and isPrime(N):
        print(N)
        break

    N += 1

# N = int(input())

# if N == 1:
#     print(2)
#     exit()

# sieve = [False] * int(100 * 1.3) # 걸러졌다 = True
# for i in range(2, len(sieve)):    
#     if sieve[i]:
#         continue

#     for j in range(2, len(sieve)//i):
#         sieve[i*j] = True

# for i in range(N, len(sieve)):
#     if str(i) != str(i)[::-1]:
#         continue

#     if sieve[i] == False:
#         print(i)
#         break