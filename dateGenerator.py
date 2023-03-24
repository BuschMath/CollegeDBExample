import random

def generateRandomDate():
    year = random.randint(1950, 2005)
    month = random.randint(1,12)
    
    if month == 1 or month == 3 or month == 5 or month == 7 or month == 8 or month == 10 or month == 12:
        day = random.randint(1,31)
    elif month == 4 or month == 6 or month == 9 or month == 11:
        day = random.randint(1,30)
    else:
        day = random.randint(1,28)

    date = str(year) + '-' + str(month) + '-' + str(day)

    return date