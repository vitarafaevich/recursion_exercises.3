import turtle


def square(size):
    if size <= 1:
        return None
    for _ in range(4):
        turtle.fd(size)
        turtle.right(90)
    turtle.right(10)
    turtle.up()
    turtle.fd(size*0.05)
    turtle.pd()
    square(size - 10)


def main_square():
    turtle.up()
    turtle.goto(0, 0)
    turtle.pd()
    a = int(input('Длина стороны:'))
    square(a)
    turtle.done()


main_square()


turtle.speed(200)
def fraktal(order, size):
    if order == 0:
        turtle.forward(size)
    else:
        fraktal(order-1, size)
        turtle.left(90)
        fraktal(order-1, 2*size/3)
        turtle.right(180)
        fraktal(order-1, 2*size/3)
        turtle.left(90)
        fraktal(order-1, size)


def main():
    turtle.up()
    turtle.goto(-100, -200)
    turtle.down()
    n = int(input('Глубина рекурсии:'))
    a = int(input('Длина стороны:'))
    fraktal(n, a)
    turtle.done()


main()