def pownum(number, deg):
    if deg == 0:
        return 1
    elif deg == 1:
        return number
    else:
        return (number * pownum(number, deg - 1))


number = int(input('enter number '))
deg = int(input('enter degree for number '))
print('result', pownum(number, deg))

'''
накапливаем произведение числа, те
5 * pownum(5, 2)
5 * 5 * 5
'''
