# 1
data = "\"c:\\python_project\\test\""
print(data)
# 원하는 출력문
# "c:\python_project\test"

# 2
total_count = int(input('게시글의 총 갯수를 입력하세요 :'))
one_page_count = int(input('한 페이지에 필요한 게시글 수를 입력하세요 : '))

page = int(total_count/one_page_count)
print(page)

# 3
person1 = input("첫 번째 사람의 이름을 입력하시오: ")
person2 = input("두 번째 사람의 이름을 입력하시오: ")


# print(f"{person1}\n\n{person2}")
print(person1, person2, sep="\n\n\n")

# 4
multiple = []
i = 1
while 2 * i < 1000:
  multiple.append(2 * i)
  i += 1

j = 1
while j * 7 < 1000:
  multiple.append(7 * j)
  j += 1

# 중복제거 및 총합
multiple = list(set(multiple))
multiple = sum(multiple)

print(multiple)

# 5
m = 5 #세로
n = 4 #가로

# ****
# ****
# ****
# ****
# ****

for i in range(5):
  print('****')
