words_dict = {'proper' : '적절한',
'possible' : '가능한',
'moral' : '도덕적인',
'patient' : '참을성 있는',
'balance' : '균형',
'perfect' : '완벽한',
'logical' : '논리적인',
'legal' : '합법적인',
'relevant' : '관련 있는',
'responsible' : '책임감 있는',
'regular' : '규칙적인'}

for k in words_dict:
  if k[0] in ['b', 'm', 'p']:
    new_k = 'im' + k[1:]
    words_dict[new_k] = words_dict[k]
    del words_dict[k]
  # elif k[0] == 'l':
  #   new_k = 'il' + k[1:]
  #   words_dict[new_k] = words_dict.pop[k]
  # elif k[0] == 'r':
  #   new_k = 'ir' + k[1:]
  #   words_dict[new_k] = words_dict.pop[k]

print(words_dict)
