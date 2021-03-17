def perfectSquare(n):
    x = n
    if n < 1:
        return False
    else:
        for i in range(int(n / 2) + 1):
            if (i * i) == n:
                return True
        return False

    return (int(x ** 0.5)) ** 2 == x


def methodFerma(n):
    s = int(n ** 0.5) + 1
    k = 0
    while not perfectSquare(((s+k) ** 2) - n):
        k += 1
    y_sqrt = int((((s+k) ** 2) - n) ** 0.5)
    a = int((s+k) - y_sqrt)
    b = int((s+k) + y_sqrt)
    print(a, b)
    return

