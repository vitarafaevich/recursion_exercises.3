def odd_list(a, n):
    if n >= len(a):
        return []
    if a[n] % 2 == 0:
        return [n] + odd_list(a, n + 1)
    else:
        return odd_list(a, n + 1)


a = list(map(int, (input("enter the list items separated by a space ").split())))
n = 0

print(odd_list(a, n))
