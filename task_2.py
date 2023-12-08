def count(num):
    if num < 10:
        return 1
    else:
        future_num = num / 10
        return 1 + count(future_num)


num = int(input('enter number '))
print(count(num))
