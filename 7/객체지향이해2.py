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

print(collatz(6)) #=> 8
print(collatz(16)) #=> 4
print(collatz(27)) #=> 111
print(collatz(626331)) #=> -1