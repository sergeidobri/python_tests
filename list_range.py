def list_of_numbers(n: int) -> list:
    if type(n) is not int:
        raise TypeError('граница списка должна быть целым числом')
    if n < 0:
        return [*range(-1, n-1, -1)]
    return [*range(1, n+1)]


if __name__ == '__main__':
    print(list_of_numbers(2))