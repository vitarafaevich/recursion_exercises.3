def ten_to_bin(x):
    if x == 0:
        return []
    if x % 2 == 0:
        return [0] + ten_to_bin(x/2)
    else:
        return [1] + ten_to_bin(x//2)


x = int(input('enter a number to transfer it to the x2 system '))

res = ten_to_bin(x)
result = ''.join(map(str, res[::-1]))
print(result)
