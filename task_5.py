def mod_number(nat_num, nat_num_2):
    if nat_num < nat_num_2:
        return nat_num
    else:
        return mod_number(nat_num - nat_num_2, nat_num_2)


nat_num = int(input('enter the first natural number '))
nat_num_2 = int(input('enter the second natural number '))

print('the remainder of the division is', mod_number(nat_num, nat_num_2))
