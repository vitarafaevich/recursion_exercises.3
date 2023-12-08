def progress(a_1, dif, num):
    if num == 1:
        return a_1
    elif num <= 0:
        return 0
    else:
        return a_1 + progress(a_1 + dif, dif, num - 1)


a_1 = int(input('enter the first member of the sequence '))
dif = int(input('enter the difference between members of the sequence '))
num = int(input('enter the number of the member you want to find '))

print('the sum of the ', num, 'members of the sequence is ', progress(a_1, dif, num))
