


PI = 22 / 7

def degree_to_radian(degrees):
    return degrees * (PI / 180)

def factorial(n):
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result

def sine(x, terms=10):
    result = 0
    for n in range(terms):
        result += ((-1) ** n) * (x ** (2 * n + 1)) / factorial(2 * n + 1)
    return result

def cosine(x, terms=10):
    result = 0
    for n in range(terms):
        result += ((-1) ** n) * (x ** (2 * n)) / factorial(2 * n)
    return result
