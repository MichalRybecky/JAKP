def uroky(doba, vynos, interval='y', kapital=0, prispevok=0, dan=False, vyska_dane=0):
    """
    WORK IN PROGRESS
    """
    results = []
    vynos, dan = vynos / 100, dan / 100
    if not dan:
        vyska_dane = 0
    for i in range(doba):
        results.append(kapital)
        kapital += (kapital * vynos) - (kapital * vynos * dan)