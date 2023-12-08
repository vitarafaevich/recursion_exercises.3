def degree5(num, cnt=1):
    if num % 5 != 0:
        return -1
    else:
        new_c = cnt + 1
        return degree5(num / 5, new_c)



num = int(input('enter number '))
print(degree5(num, cnt=1))


'''
def power5(N):
    if N == 1:
        return 0
    elif N % 5 != 0:
        return -1
    else:
        res = power5(N // 5)
        if res == -1:
            return -1
        else:
            return res + 1
'''