def ten_to_bin(x):
    if x == 0:
        return(0)
    else:
        binary = ten_to_bin(x // 2)
        return binary + str(x % 2)

x = 375
binary = ten_to_bin(x)
print(binary)