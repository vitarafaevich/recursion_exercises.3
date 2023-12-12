def simmetr(s, i, j):
    if i >= j:
        return True
    elif s[i] == s[j]:
        return simmetr(s, i+1, j-1)
    else:
        return False


s = input()
i = int(input())
j = int(input())

print(simmetr(s, i, j))
