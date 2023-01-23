# 1
def change_fresh_fruit(fruits):
  if fruits == '':
    return []
  fruits = list(map(str, fruits.lower().split(',')))
  
  for i in range(0, len(fruits)):
    if 'rotten' in fruits[i]:
      fruits[i] = fruits[i][6:].lower()
  return fruits

print(change_fresh_fruit('apple,rottenBanana,apple,RoTTenorange,Orange'))
print(change_fresh_fruit(''))

# 2
def middle_char(str):
  if len(str) % 2 == 0:
    idx = int(len(str)/2 - 1)
    print(str[idx:idx + 2])
  else:
    idx = int(len(str)/2)
    print(str[idx])

middle_char('abcd')
middle_char('abcde')

# 3
infos = [{'name': 'kim', 'age': 12}, {'name': 'lee', 'age': 4}]

ages = []
for info in infos:
  for key, value in info.items():
    if key == 'age':
      ages.append(value)

ages = sum(ages)
print(ages)

# 4
def blood_types_dic(blood_types):
  dic = {}
  for type in blood_types:
    if not type in dic:
      dic[type] = 1
    else:
      dic[type] += 1
  return dic

blood_types = ['A','A','O', 'B', 'A', 'O', 'AB','O', 'A', 'B', 'O', 'B', 'AB']
print(blood_types_dic(blood_types))

# 5
# 소금물의 퍼센트 농도와 소금물의 양
percent = list(map(int, input('소금물의 퍼센트 농도를 입력하세요: ').split(' ')))
amount = list(map(int, input('소금물의 양을 입력하세요: ').split(' ')))

if len(percent) >= 6:
  percent = percent[:5]
  print('최대 5개의 소금물을 입력할 수 있습니다.')
if len(amount) >= 6:
  amount = amount[:5]
  print('최대 5개의 소금물을 입력할 수 있습니다.')

# 혼합된 소금물의 농도 / 양을 계산
def mix(percent, amount):
  zip_list = list(zip(percent, amount)) # [(1, 2), (3, 4), (5, 7)] (농도, 양)

  # 총 소금의 양
  salt_list = []
  for percent, amount in zip_list:
    salt_list.append(percent * amount / 100)
  total_salt = sum(salt_list)

  # 총 소금물 양
  total_amount = 0
  for i in range(len(zip_list)):
    total_amount += zip_list[i][1]

  # 총 소금물 농도
  total_percent = round(total_salt / total_amount * 100, 2)

  return (f'혼합된 소금물의 농도는 {total_percent}% 이고 소금물의 양은 {total_amount}입니다')

print(mix(percent, amount))
  