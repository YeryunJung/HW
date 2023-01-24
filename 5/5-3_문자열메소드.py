# 입력 예시
s = '@#~I NeVEr DrEamEd AbouT SuCCeSs, i woRkEd foR iT.!>!'

# 출력 예시
# 'I never dreamed about success, i worked for it.'

s = s[3:-3]
s = s[:1] + s[1:].lower()

print(s)