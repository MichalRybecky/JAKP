# Kalkulacka zivota


def kalkulacka_zivota(deadline) -> dict:
    """
    Dostane datum vo formate dd/mm/yyyy a vrati dictionary s hodnotami o
    dlzke zivota
    """
    error = "Incorrect date format"
    if "/" not in deadline or len(deadline) != 10:
        return error
    deadline_list = deadline.split("/")
    if len(deadline_list) > 3:
        return error
    try:
        int(deadline_list[0])
        int(deadline_list[1])
        int(deadline_list[2])
    except ValueError:
        return error
    if int(deadline_list[0]) > 31 or int(deadline_list[1]) > 12 or int(deadline_list[2]) > 2020:
        return error

    import datetime
    currentDate = datetime.datetime.now()

    # v takejto forme to potrebujeme deadline ('Plz enter your date of birth (dd/mm/yyyy) ')
    deadlineDate = datetime.datetime.strptime(deadline, "%d/%m/%Y")
    daysLeft = currentDate - deadlineDate

    years = (daysLeft.total_seconds()) / (365.242 * 24 * 3600)
    yearsInt = int(years)

    months = (years) * 12
    monthsInt = int(months)

    days = (months) * (365.242 / 12)
    daysInt = int(days)
    
    weeks = (days) / 7
    weeksInt = int(weeks)

    hours = (days) * 24
    hoursInt = int(hours)

    minutes = (hours) * 60
    minutesInt = int(minutes)

    seconds = (minutes) * 60
    secondsInt = int(seconds)

    milliseconds = (seconds) * 1000
    millisecondsInt = int(milliseconds)

    return {
        "years": round(years, 2),
        "months": round(months, 2),
        "weeks": round(weeks, 1),
        "days": round(days),
        "hours": round(hours),
        "minutes": round(minutes),
        "seconds": round(seconds),
        "miliseconds": round(milliseconds),
    }







