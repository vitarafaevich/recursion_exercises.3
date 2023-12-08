def maxlist(a):
    if len(a) == 1:
        return a
    if (a[len(a) - 1]) > (a[len(a) - 2]):
        del a[len(a) - 2]
        return maxlist(a)
    else:
        del a[len(a) - 1]
        return maxlist(a)
    print(a)



a = [x for x in input('enter the list items separated by a space ').split()]

print(maxlist(a))
