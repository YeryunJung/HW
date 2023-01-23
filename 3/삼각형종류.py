s_triangle = list(map(int, input('각 변을 입력해주세요: ').split(' ')))

def triangle_type(s_triangle):
  no_duplication = list(set(s_triangle))
  if len(no_duplication) == 1:
    return('정삼각형')
  elif len(no_duplication) == 2:
    return('이등변삼각형')

  max_side = max(s_triangle)
  s_triangle.remove(max_side)
  if s_triangle[0]**2 + s_triangle[1]**2 == max_side**2:
    return('직각삼각형')
  elif s_triangle[0] + s_triangle[1] > max_side:
    return('삼각형')
  else:
    return('삼각형 아님')

print(triangle_type(s_triangle))
  