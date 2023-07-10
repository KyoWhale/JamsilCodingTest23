# 13:52 ~ 14:29 뜯어고침
# 14:29 ~ 14:52 X
# 14:53 ~ 14:58 https://puleugo.tistory.com/29

minus_split = input().split('-')
answer = sum(map(int, minus_split[0].split('+')))
for part in minus_split[1:]:
    answer -= sum(map(int, part.split('+')))
print(answer)

# sentence = input()
# split = sentence.split('-')
# for i in range(len(split)-1, -1, -1):

# for i in range(len(split)):
#     split[i] = split[i].split('+')

# sentence = ''
# for sub in split:
#     print(sub)

# total = 0
# while sentence:
#     if sentence[0] != '-':
#         next_minus = sentence.find('-')
#         if next_minus == -1:
#             total += eval(sentence)
#             sentence = ""
#         else:
#             total += eval(sentence[:next_minus])
#             sentence = sentence[next_minus:]
#     else:
#         next_minus = sentence.find('-',1)
#         if next_minus == -1:
#             total -= eval(sentence[1:])
#             sentence = ""
#         else:
#             total -= eval(sentence[1:next_minus])
#             sentence = sentence[next_minus:]


# print(total)

# -10+10 | -10