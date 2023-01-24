# A.    입력 예시 
# ['eat','tea','tan','ate','nat','bat']

# B.    출력 예시 
# [ ['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat'] ] 

word_list = input('리스트를 입력하세요: ')

def group_anagrams(word_list):
    word_list = word_list.replace('[', '')
    word_list = word_list.replace(']', '')
    word_list = word_list.replace("'", '')
    word_list = list(map(str, word_list.split(',')))
    
    dic = {}
    for word in word_list:
        sorted_word = "".join(sorted(word))
        if not sorted_word in dic:
            dic.setdefault(sorted_word, [word])
        else:
            dic[sorted_word].append(word)
    return list(dic.values())

print(group_anagrams(word_list))


###########################################################
# solving

# words = list(input('리스트를 입력하세요: '))

# def anagram(words):
#     anagrams = {}

#     for word in words:
#         key = ''.join(sorted(word))
#         anagrams.setdefault(key, [])  # 각각의 키가 밸류 값을 가지도록 디폴트를 설정
#         anagrams[key].append(word)
#     return list(anagrams.values())

# print(def anagram(words))