def count(n):
    if n < 10:
        return 1
    else:
        future_num = n / 10
        return 1 + count(future_num)


n = int(input('enter number '))
print(count(n))

