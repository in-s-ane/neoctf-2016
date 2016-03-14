yr = 2016
month = 1
day = 1
bars = 0

thirtyDays = [2, 4, 6, 9, 11]
thirtyOneDays = [1,3,5,7,8,10,12]

def isCube(n):
    x = int(round(n ** (1/3)))
    return x ** 3 == n

def isSquare(n):
    x = int(round(n ** (1/2)))
    return x ** 2 == n

def sumDigits(n):
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s


while month < 13:
    s = sumDigits(yr) + sumDigits(month) + sumDigits(day)

    if (isCube(s) or isSquare(s) or (month == 12 and day == 25)):
        pass
    else:
        bars += s

    day += 1

    if month == 2 and day == 29:
        month += 1
        day = 1

    if month in thirtyDays and day == 30:
        month += 1
        day = 1

    if month in thirtyOneDays and day == 31:
        month += 1
        day = 1

print bars
