x = []


def read_file(string):
    global x
    f = open(string, 'r')
    x = f.read().split(" ")
    x = [int(i) for i in x]
    f.close()


def hoocne_multiply(arr):
    b = [1, -arr[0]]
    k = 1
    while k < len(arr):
        b.append(0)
        a = [b[0]]  # an = bn
        c = arr[k]
        for i in range(1, len(b)):
            a_k = b[i] - b[i - 1] * c  # a_k = b_k - b_(k + 1) * c
            a.append(a_k)
        print(a)
        b = a.copy()
        k += 1


read_file('input.txt')

hoocne_multiply(x)
