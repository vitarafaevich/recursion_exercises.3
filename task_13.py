def odd_list(a):
    if a[0] % 2 == 0:
        return [a[0]] + odd_list(a[1:])
    else:
        return odd_list(a[1:])


a = input("enter the list items separated by a space ").split()
a = list(map(int, a))

print(a)
print(odd_list(a))