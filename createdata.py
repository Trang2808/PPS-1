from math import exp, sin, cos, tan, pi
import random 


def f(x):
    # return 5 * x**4 + x**3 + 2 * x**2 + 3 * x + 4
    # return x ** 2 * exp(1 / 2 * (x ** 2)) + cos(x ** 2) * tan(x) - 5 * exp(x)
    return x ** 5 

def write_input_x_y(a, b): # mốc nội suy cách đều 1 đơn vị trong đoạn a b
    g = open("input_test.txt", "w")
    for x in range(a, b):
        y = f(x)
        g.write(f'{x} {y}\n')
    g.close()

def write_set_input_x_equally(a, b, h): # mốc nội suy cách đều 1 đoạn bằng h trong đoạn a, b
    g = open("input_equally.txt", "w")
    x = a
    i = 1
    while True:
        y = f(x)
        g.write(f'{x} {y}\n')
        x = a + i * h
        i += 1
        if x > b: break
    g.close()

def write_set_input_x_any(n, a, b): # n mốc nội suy random bất kỳ trong đoạn (a,b)
    g = open("input_random.txt", "w")
    for i in range(n):
        x = random.uniform(a, b)
        y = f(x)
        g.write(f'{x} {y}\n')
    g.close()

def write_optimized_x(n, a, b): # n mốc nội suy tối ưu trong đoạn a,b
    g = open("input_optimization.txt", "w")
    x = []
    for i in range(n):
        temp = 1 / 2 * ((b - a) * cos(((2 * i + 1) * pi) / (2 * (n + 1))) + (b + a))
        x.append(temp)
    for j in x:
        y = f(j)
        g.write(f'{j} {y}\n')
    g.close()

write_input_x_y(1, 7)
write_optimized_x(15, 2, 8)
write_set_input_x_equally(2.0, 7, 0.2)
write_set_input_x_any(10, 2, 8)
