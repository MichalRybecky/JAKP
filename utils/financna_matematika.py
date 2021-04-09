def uroky(kapital, doba, urok, interval_uroku='y', prispevok=0, interval_prispevku='y', dan=False, vyska_dane=0):
    results = []
    urok, dan = urok / 100, dan / 100
    if not dan:
        vyska_dane = 0
    if interval_uroku == interval_prispevku:
        for i in range(doba+1):
            results.append(round(kapital, 2))
            kapital += (kapital * urok) - (kapital * urok * dan)
            kapital += prispevok
    elif interval_uroku == 'y' and interval_prispevku == 'm':
        for i in range(doba+1):
            results.append(round(kapital, 2))
            kapital += prispevok * 12
            kapital += (kapital * urok) - (kapital * urok * dan)
    elif interval_uroku == 'm' and interval_prispevku == 'y':
        for i in range(doba+1):
            results.append(round(kapital, 2))
            kapital += (kapital * urok) - (kapital * urok * dan)
            if doba % 12 == 0 and doba != 0:
                kapital += prispevok
    return results
