def ten_to_two(x):
    if 2 <= n <= 9:
        if x == 0:
            return []
        else:
            return [x % n] + ten_to_two(x / n)



x = int(input('enter a number to transfer it to the x2 system '))
n = int(input('in what system are we going '))

res = ten_to_two(x)
result = ''.join(map(str, res[::-1]))
print(result)