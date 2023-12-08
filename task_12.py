def search(a, x):
    if not a:
        print(0)
    elif a[0] == x:
        print(1)
    else:
        return search(a[1:], x)


a = input("enter the list items separated by a space ").split()
a = list(map(int, a))
x = int(input('put down a number you want to check is in the list '))

search(a, x)