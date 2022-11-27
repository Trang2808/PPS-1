from math import *


def f(x):
    return x**2
    # return 5 * x**4 + x**3 + 2 * x**2 + 3 * x + 4
    # return x ** 2 * exp(1 / 2 * (x ** 2)) + cos(x ** 2) * tan(x) - 5 * exp(x)


def write_input_x_y(a, b):
    g = open("input.txt", "w")
    for x in range(b, a, -1):
        y = f(x)
        g.write(f'{x} {y}\n')
    g.close()


def write_optimized_x(n, a, b):
    g = open("input.txt", "w")
    x = []
    for i in range(n):
        temp = 1 / 2 * ((b - a) * cos(((2 * i + 1) * pi) / (2 * (n + 1))) + (b + a))
        x.append(temp)
    for j in x:
        y = f(j)
        g.write(f'{j} {y}\n')
    g.close()


write_input_x_y(1, 7)
# write_optimized_x(6, 2, 5)
