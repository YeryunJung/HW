# # 1
# def input_password():
#   count = 3
#   for i in range(0, 3):
#     try:
#       password = input('비밀번호를 입력해주세요: ')
#       if password == '1234':
#         print('비밀번호가 일치합니다.')
#         return
#       elif password != '1234':
#         count -= 1
#         if count == 0:
#            print('입력기회가 종료되었습니다.')
#            return
#         print(f'잘못된 비밀번호입니다.\n입력기회가 {count}번 남았습니다.')
#     except:
#       count -= 1
#       print(f'숫자를 입력해주세요.\n입력기회가 {count}번 남았습니다.')

# input_password()

# # 2
# students = [
#     '박해피',
#     '이영희',
#     '조민지',
#     '조민지',
#     '김철수',
#     '이영희',
#     '이영희',
#     '김해킹',
#     '박해피',
#     '김철수',
#     '한케이',
#     '강디티',
#     '조민지',
#     '박해피',
#     '김철수',
#     '이영희',
#     '박해피',
#     '김해킹',
#     '박해피',
#     '한케이',
#     '강디티',
# ]

# def vote_ranking(students):
#   dic = {}
#   for student in students:
#     if not student in dic:
#       dic[student] = 1
#     else:
#       dic[student] += 1
#   # 득표수대로 출력
#   for k in dic:
#     print(k)

# print(vote_ranking(students))

# # 3
# # 입력 예시
# # [1, 1, 3, 3, 0, 1, 1]

# # 출력 예시
# # [1, 3, 0, 1]

# def new_list(list):
#   result = []
#   for el in list:
#     if len(result) == 0:
#       result.append(el)
#     elif len(result) > 0 and el != result[-1]:
#       result.append(el)
#     else:
#       pass
#   return result

# print(new_list([1, 1, 3, 3, 0, 1, 1]))

# # 4
# word1 = input('첫 번째 이름을 입력하세요 : ')
# word2  = input('두 번째 이름을 입력하세요 : ')

# # 파이썬 빌트인 함수
# # ord('a') = 97
# # chr(97) = 'a'

# def ascii(word1, word2):
#   word1_list = list(word1)
#   word2_list = list(word2)

#   word1_sum = 0
#   for word in word1_list:
#     word1_sum += ord(word)

#   word2_sum = 0
#   for word in word2_list:
#     word2_sum += ord(word)

#   if word1_sum > word2_sum:
#     return word1
#   else:
#     return word2  

# print(ascii(word1, word2))

# 5
test_status = {
    '김싸피': 'solving',
   	'이코딩': 'solving',
   	'최이썬': 'cheating',
   	'오디비': 'sleeping',
   	'임온실': 'cheating',
   	'조실습': 'solving',
   	'박장고': 'sleeping',
   	'염자바': 'cheating'
}

def coding_test(test_status):
  cheating = []
  # 커닝하는 사람 제거
  for k in test_status.copy():
    if test_status[k] == 'cheating':
      cheating.append(k)
      del test_status[k]
  # 커닝하는 사람 리스트 오름차순으로 출력
  cheating.sort()
  # 잠자는 사람 깨우기
  for k in test_status.copy():
    if test_status[k] == 'sleeping':
      test_status[k] = 'solving'
  return (f'{cheating}\ntest_status = {test_status}')

print(coding_test(test_status))



