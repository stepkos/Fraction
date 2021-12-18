def NWD(a, b):
    while b:
        a, b = b, a % b
    return a


def NWW(a, b):
    return a * b / NWD(a, b)
