x = []


def read_file(string):
    global x
    f = open(string, 'r')
    x = f.read().split(' ')
    x = [int(i) for i in x]
    f.close()


def hoocne_divive(arr, c):
    b = [arr[0]]  # b_0 = a_0
    for i in range(1, len(arr)):
        b_k = arr[i] + b[i - 1] * c  # b_k = a_k + b_k-1 * c
        b.append(b_k)
    return b


def Degf_k(arr, k, c):
    factorial = 1
    for i in range(1, k + 1):
        arr = hoocne_divive(arr, c)
        arr.pop()  # lay dao ham nen bo gia tri cuoi di
        factorial *= i
    res = hoocne_divive(arr, c).pop()  # lay gia tri tai c
    return factorial * res



read_file('input1.txt')
hoocne_divive(x, 5)

