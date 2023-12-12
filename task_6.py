def degree5(num):
    if num == 1:
        return 0
    elif num % 5 != 0:
        return -1
    elif num % 5 == 0:
        param = degree5(num / 5)

        if param != -1:
            return 1 + degree5(num / 5)
        else:
            return -1

num = int(input('enter number '))
print(degree5(num))
