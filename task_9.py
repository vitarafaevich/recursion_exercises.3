def combin(n, k):
    if n == 0 or k == 0:
        return 1
    else:
        return((combin(n - 1, k)) + (combin(n - 1, k - 1)))


n = int(input('enter the first number '))
k = int(input('enter the first number '))

print(combin(n, k))