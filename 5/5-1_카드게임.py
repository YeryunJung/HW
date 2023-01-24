# 1
import random

def making_card_list() -> list:
	card_list = []

	for shape in ["spade", "heart", "diamond", "clover"]:

		for number in ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]:

			card_list.append((shape, number))

	return card_list

trump_card_list = making_card_list()
trump_card_count = len(trump_card_list) - 1 # 51

# random 모듈로 무작위 추첨
# random.randrange(0, 52)
# random.choice(trump_card_list)

# 승자 판단 함수
def game_judgment(player1, player2):
  alphabet = ['A', 'K', 'Q', 'J']
  shape = ['spade', 'diamond', 'heart', 'clover']

  # 숫자와 문자 비교
  if type(player1[1]) == str and type(player2[1]) == int:
    return(f'{player1} {player2} player1 win!')
  elif type(player1[1]) == int and type(player2[1]) == str:
    return(f'{player1} {player2} player2 win!')
  # 둘다 숫자일 때 숫자 비교
  elif type(player1[1]) == int and type(player2[1]) == int:
    if player1[1] > player2[1]:
      return(f'{player1} {player2} player1 win!')
    elif player1[1] < player2[1]:
      return(f'{player1} {player2} player2 win!')
  # 둘다 문자일 때 비교
  elif type(player1[1]) == str and type(player2[1]) == str:
    if alphabet.index(player1[1]) < alphabet.index(player2[1]):
      return(f'{player1} {player2} player1 win!')
    elif alphabet.index(player1[1]) > alphabet.index(player2[1]):
      return(f'{player1} {player2} player2 win!')
      # 문자까지 같을 때 모양 비교
    elif alphabet.index(player1[1]) == alphabet.index(player2[1]):
      if shape.index(player1[0]) < shape.index(player2[0]):
        return(f'{player1} {player2} player1 win!')
      elif shape.index(player1[0]) > shape.index(player2[0]):
        return(f'{player1} {player2} player2 win!')

# 승자 출력 및 총 결과 출력
def total_winner():
  player1_win = 0
  player2_win = 0
  while player1_win < 6 and player2_win < 6:
    player1 = random.choice(trump_card_list) # ('heart', 6)
    player2 = random.choice(trump_card_list) # ('diamond', 'Q')
    judgment = game_judgment(player1, player2)
    print(judgment)
    if 'player1' in judgment:
      player1_win += 1
    else:
      player2_win += 1

  if player1_win == 6:
    return(f'{player1_win}:{player2_win} Finally player1 win')
  elif player2_win == 6:
    return(f'{player2_win}:{player1_win} Finally player2 win')

print(total_winner())
