# num_list = [4, 4, 7, 8, 10, 4]
# sum_of_repeat_number(num_list)

# 출력 예시 
#  25

def sum_of_repeat_number(num_list):
  deduplicate_list = []
  for num in num_list:
    if num_list.count(num) > 1:
      pass
    else:
      deduplicate_list.append(num)
  return sum(deduplicate_list)

num_list = [4, 4, 7, 8, 10, 4]
print(sum_of_repeat_number(num_list))