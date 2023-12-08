def numbers(x):
    if x < 10:
        print(x)
    else:
        print(x % 10)
        numbers(x // 10)


x = int(input('enter the list items separated by a space '))
print(numbers(x))
