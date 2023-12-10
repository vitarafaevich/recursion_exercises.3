list = ()


def ten_to_bin(x, res=None):
    if res is None:
        res = []
    if x // 2 == 0:
        res.append()
    elif x % 2 == 1:
        return ten_to_bin(res.append(1), (x // 2))
    elif x % 2 == 0:
        return ten_to_bin(res.append(0), (x // 2))
    return res


res = None
x = int(input())

print(ten_to_bin(x, res))