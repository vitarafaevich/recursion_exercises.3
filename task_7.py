def nod(num_1, num_2):
    if num_1 == 0 or num_2 == 0:
        return("can't be found")
    elif num_1 == num_2:
        return num_1
    elif num_2 == 0:
        return num_1
    else:
        if num_1 < num_2:
            num_1, num_2 = num_2, num_1
        return nod(num_2, num_1 % num_2)


num_1 = int(input('enter the first number '))
num_2 = int(input('enter the second number '))

print(nod(num_1, num_2))
