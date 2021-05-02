def kvadraticka_rovnica(a, b, c):
    if type(a) != int or type(b) != int or type(c) != int:
        raise TypeError("Arguments must be of type int")
    diskriminant = b ** 2 - (4 * a * c)
    return [diskriminant, ((-b) + diskriminant ** 0.5) / (2 * a), ((-b) - diskriminant ** 0.5) / (2 * a)]
