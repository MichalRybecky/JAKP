import statistics

def median(x):
    """
    Vrati median z listu cisel, napr.\n
    median([2, 3, 4, 5]) == 3.5
    """
    return statistics.median(x)

def modus(x):
    """
    Vrati modus (najcastejsiu hodnotu) z listu cisel, napr.
    modus([2, 3, 4, 5, 2]) == 2
    """
    return statistics.mode(x)

def priemer(x):
    """
    Vrati aritmeticky priemer z listu cisel, napr.
    priemer([1, 2, 3, 4, 5]) == 3
    """
    return statistics.mean(x)