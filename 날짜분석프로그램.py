# 입력 예시
# 2015
# 8
# 31

# 출력 예시 
# 경고 월요일입니다.
# {'년': 2015, '월': 8, '일': 31, '요일': '월요일'}

import calendar

# 요일 추출하는 함수
def get_day(yyyy, mm, dd):
    days = ['월요일', '화요일', '수요일', '목요일', '금요일', '토요일', '일요일']
    return days[calendar.weekday(yyyy, mm, dd)]

year = int(input('연도를 입력해주세요: '))
if ((year % 4 == 0) and (year % 100 != 0) or (year % 100 == 0)):
    year = int(input('윤년입니다. 연도를 다시 입력해주세요: '))
else:
    print(calendar.calendar(year))

month = int(input('월을 입력해주세요: '))

day = int(input('요일을 입력해주세요: '))
dayname = get_day(year, month, day)
# 월요일 경고 출력
if dayname == '월요일':
    print('경고 월요일입니다.')
    
print({'년': year, '월': month, '일': day, '요일': dayname})

