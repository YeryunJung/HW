def collatz(num):
    count = 0

    while num != 1:
        if num % 2:
            count += 1
            num = num * 3 + 1
        else:
            count += 1
            num = int(num / 2)

    if count >= 500:
        return -1
        
    return count

##################################################
# solving1

def collatz(num):
    for i in range(500):
        if num % 2 == 0:
            num = num / 2
        else: # 홀수
            num = (num * 3) + 1

        if num == 1:
            return i + 1 # 인덱스가 0부터 시작했으니까

    return -1

# solving2

def collatz(num):
    if num == 1:
        return 0

    ans = 0

    if num % 2 == 0:
        num //= 2
        ans = collatz(num)
        if ans != -1:
            ans += 1

    elif num % 2 == 1:
        num = num * 3 + 1
        ans = collatz(num)
        if ans != -1:
            ans += 1

    if ans > 500:
        return -1

    return ans


print(collatz(6)) #=> 8
print(collatz(16)) #=> 4
print(collatz(27)) #=> 111
print(collatz(626331)) #=> -1