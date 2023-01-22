words = ["round" , "dream", "magnet" , "tweet" , "tweet", "trick", "kiwi"]

#앞 단어 마지막 글자 = 뒷 단어 첫 글자일 경우 통과
#앞 단어 마지막 글자 != 뒷 단어 첫 글자일 경우 패배
#이전 썼던 단어 쓰는 경우 (words 리스트 안에 있을 경우) 패배
#done을 입력하는 경우 끝

result = 0
for i in range(1, len(words)): # 1, 2, 3, 4, 5, 6
    idx = len(words[i - 1]) - 1
    last = words[i - 1][idx]
    first = words[i][0]
    if last != first:
        result = i + 1
        print(f'{result} 번째 사람이 패배입니다')
        break
    elif words.count(words[i]) >= 2:
        result = i + 1
        print(f'{result} 번째 사람이 패배입니다')
        break
    elif words[i] == 'done':
        print('경기 종료입니다')
        break
    else:
        continue
if not result:
    print('경기 종료입니다')


# idx = 0
# word_idx = len(words) - 1 # index는 0부터 시작하기 때문에 리스트의 길이에서 - 1

# while idx < word_idx:
#     idx += 1
#     if words[idx - 1][-1] != words[idx][0] or words[idx] in word[:idx]:
#         print(f'{idx + 1}번째 참가자가 탈락')
#         break
#     elif idx == word_idx: # 만약 아무도 탈락하지 않고 끝까지 진행이 됐다면
#         print('아무도 탈락하지 않았다')