# Kalkulacka zivota


def kalkulacka_zivota(deadline) -> dict:
    """
    Dostane datum vo formate dd/mm/yyyy a vrati dictionary s hodnotami o
    dlzke zivota
    """

    import datetime
    currentDate = datetime.datetime.now()

    # v takejto forme to potrebujeme deadline ('Plz enter your date of birth (dd/mm/yyyy) ')
    deadlineDate = datetime.datetime.strptime(deadline, "%d/%m/%Y")
    print(deadlineDate)
    daysLeft = currentDate - deadlineDate
    print(daysLeft)

    years = (daysLeft.total_seconds()) / (365.242 * 24 * 3600)
    yearsInt = int(years)

    months = (years) * 12
    monthsInt = int(months)

    days = (months) * (365.242 / 12)
    daysInt = int(days)

    hours = (days) * 24
    hoursInt = int(hours)

    minutes = (hours) * 60
    minutesInt = int(minutes)

    seconds = (minutes) * 60
    secondsInt = int(seconds)

    milliseconds = (seconds) * 1000
    millisecondsInt = int(milliseconds)

    return {
        "years": years,
        "months": months,
        "days": days,
        "hours": hours,
        "minutes": minutes,
        "seconds": seconds,
        "miliseconds": milliseconds,
    }
