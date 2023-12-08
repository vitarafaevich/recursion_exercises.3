def fib(num):
    if num == 1 or num == 2:
        return 1
    else:
        return(fib(num - 2) + fib(num - 1))


num = int(input('enter the number of the member of Fibonacci seqence you want to find '))

print(fib(num))
