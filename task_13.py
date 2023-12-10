def odd_list(a):
    if not a:
        return []
    else:
        if a[0] % 2 == 0:
            return [a[0]] + odd_list(a[1:])
        else:
            return odd_list(a[1:])


a = list(map(int, (input("enter the list items separated by a space ").split())))

print(odd_list(a))
