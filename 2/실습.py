# 1
a = 3
b = 6
c = -5

quadratic_equation1 = (-b + (b**2 - 4*a*c)**0.5) / (2*a)
quadratic_equation1 = round(quadratic_equation1, 4)
quadratic_equation2 = (-b - (b**2 - 4*a*c)**0.5) / (2*a)
quadratic_equation2 = round(quadratic_equation2, 4)

print((quadratic_equation1, quadratic_equation2))

# 2
# 입력 예시
# <p>취업 준비생에게 SW 역량 향상 교육 및 다양한 취업지원 서비스를 제공하여 취업에 성공하도록 돕는 프로그램입니다.</p>

# 출력 예시
# 취업 준비생에게 SW 역량 향상 교육 및 다양한 취업지원 서비스를 제공하여 취업에 성공하도록 돕는 프로그램입니다.
word = input('문장을 입력하세요: ')
word = word[3:] # 앞에서 3번째 문자부터 출력해라
word = word[:-4] # 뒤에서 4번째 글자까지 잘라내라
print(word)

# 3
str_lst = input('문자열을 입력하세요. : ')
str_lst = str_lst.lower()
str_lst = list(map(str, str_lst.split()))

def word_chain(str_lst):
  for i in range(1, len(str_lst)):
    if str_lst[i - 1][-1] != str_lst[i][0]:
      print('Fail')
      return
  print('Pass')

word_chain(str_lst)

# 4
# 출력 결과 예시
# 스테이크   50,000
# + VAT     7,500
# 총계 ₩    57,500

price = int(input('스테이크 가격을 입력해주세요: '))
vat = int(price * 0.15)
sum = int(price + vat)

price = (format(price, ','))
vat = (format(vat, ','))
sum = (format(sum, ','))

print(f'스테이크    {price}\n+ VAT     {vat}\n총계 ₩    {sum}')

# 5
todo = [("Python Homework", 3), ("Assay", 4), ("Vacation", 100)]

new_todo = input('해야 할 일을 입력해주세요: ')
left_days = int(input('남은 일을 입력해주세요: '))
new_tuple = (new_todo, left_days)
todo.append(new_tuple)

print(todo)
