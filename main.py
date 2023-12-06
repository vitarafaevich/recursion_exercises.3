

def pownum(number, deg):
    if number == 0:
        return 1
    elif number == 1:
        return number
    else:
        for i in range(2, deg):
            return pownum(number * number, deg)


number = int(input('enter number '))
deg = int(input('enter degree for number '))
print(pownum(number, deg))
