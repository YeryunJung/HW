orders = '아이스아메리카노,카라멜마키야또,에스프레소,아메리카노,아메리카노,아이스라떼,핫초코,아이스아메리카노,아메리카노,아이스카라멜마키야또,아이스라떼,라떼마키야또,카푸치노,라떼마키야또'

orders = list(map(str, orders.split(',')))

ice_count = 0
for order in orders:
  if '아이스' in order:
    ice_count += 1

order_count = {}
for order in orders:
  if not order in order_count:
    order_count[order] = 1
  else:
    order_count[order] += 1

print(f'아이스 음료 주문은 {ice_count}개 들어왔습니다.\n메뉴 별 주문 수는 {order_count}입니다.')

