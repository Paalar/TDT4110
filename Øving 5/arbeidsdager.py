#skuddår
def is_leap_year ( year ):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    return False


def weekday_newyear(year):
    day = 0
    start = 1900
    skudd = is_leap_year(start)
    while start != year:
        start += 1
        if skudd == False:
            day += 1
            if day % 7 == 0:
                day = 0
        elif skudd == True:
            day += 1
            if day % 7 == 0:
                day = 0
            day += 1
            if day % 7 == 0:
                day = 0
        skudd = is_leap_year(start)
    if day == 0:
        print ("Year {0} starts on a Monday".format(year))
    elif day == 1:
        print("Year {0} starts on a Tuesday".format(year))
    elif day == 2:
        print("Year {0} starts on a Wednesday".format(year))
    elif day == 3:
        print("Year {0} starts on a Thursday".format(year))
    elif day == 4:
        print("Year {0} starts on a Friday".format(year))
    elif day == 5:
        print("Year {0} starts on a Saturday".format(year))
    elif day == 6:
        print("Year {0} starts on a Sunday".format(year))
    return day

#weekday_newyear(int(input("Hvilket år skal du sjekke?")))


def is_workday(day):
    if day == 5 or day == 6:
        return True
    else:
        return False



def workdays_in_year(year):
    leap = is_leap_year(year)
    if leap == True:
        leap = 1
    else:
        leap = 0

    day = weekday_newyear(year)
    if day == 5 or day == 6:
        day = 260
    else:
        day = 261


    workdays = day + leap
    print("{0} has {1} workdays.".format(year, workdays))
    return workdays

workdays_in_year(int(input("Hvilket år skal du sjekke?")))
