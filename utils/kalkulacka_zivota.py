#Kalkulacka zivota
#tie printy mozes kludne pomazat ked si okontrolujes ako to funguje a nebudes mat namietky

import datetime
currentDate = datetime.datetime.now() #toto moze ist aj do defu()


def kalkulacka_zivota(deadline):
    #v takejto forme to potrebujeme deadline ('Plz enter your date of birth (dd/mm/yyyy) ')
    deadlineDate= datetime.datetime.strptime(deadline,'%d/%m/%Y')
    print (deadlineDate)
    daysLeft = currentDate - deadlineDate
    print(daysLeft)

    years = ((daysLeft.total_seconds())/(365.242*24*3600))
    yearsInt=int(years)

    months=(years)*12
    monthsInt=int(months)

    days=(months)*(365.242/12)
    daysInt=int(days)

    hours = (days)*24
    hoursInt=int(hours)

    minutes = (hours)*60
    minutesInt=int(minutes)

    seconds = (minutes)*60
    secondsInt =int(seconds)
    
    milliseconds = (seconds)*1000
    millisecondsInt =int(milliseconds)

    print('You are {0:d} years, {1:d}  months, {2:d}  days, {3:d}  hours, {4:d} minutes, \
{5:d} seconds, {6:d} milliseconds old.'.format(yearsInt,monthsInt,daysInt,hoursInt,minutesInt,secondsInt,millisecondsInt))
    
    #return years, months, days, hours, minutes, seconds, milliseconds


kalkulacka_zivota('21/01/2002')
