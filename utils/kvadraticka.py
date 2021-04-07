def kvadraticka_rovnica(a, b, c):
    if type(a) != int or type(b) != int or type(c) != int:
        raise TypeError("Arguments must be of type int")
    return [(-b + (b ** 2 - 4 * a * c) ** 0.5) / 2 * a, (-b - (b ** 2 - 4 * a * c) ** 0.5) / 2 * a]
