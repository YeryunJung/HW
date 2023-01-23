orders = '아이스아메리카노,카라멜마키야또,에스프레소,아메리카노,아메리카노,아이스라떼,핫초코,아이스아메리카노,아메리카노,아이스카라멜마키야또,아이스라떼,라떼마키야또,카푸치노,라떼마키야또'

orders = list(map(str, orders.split(',')))
total_num = len(orders)
no_duplicated_orders = list(set(orders))
# 내림차순
no_duplicated_orders.sort(reverse=True)

print(f'총 {total_num}잔의 주문이 들어왔습니다\n중복제거한 리스트는 {no_duplicated_orders}입니다')