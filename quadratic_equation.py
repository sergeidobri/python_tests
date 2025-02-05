def _discriminant(a, b, c):
    return b**2 - 4 * a * c

def solution(a, b, c):
    if a == 0:
        raise ValueError("Это не квадратное уравнение")
    if not set([type(a), type(b), type(c)]) <= {int, float}:
        raise TypeError("a, b, c - это числа. Целые или вещественные")
    
    discr = _discriminant(a, b, c)
    if discr > 0:
        return round((-b + _discriminant(a, b, c)**0.5)/(2*a), 2), round((-b - _discriminant(a, b, c)**0.5)/(2*a), 2)
    elif discr == 0:
        return -b/(2*a)
    else:
        return None


if __name__ == '__main__':
    print(solution(-1, -9, -15))
    print(solution(1, -13, 12))
    print(solution(-1, 16, -64))
    print(solution(12, 13, 121))