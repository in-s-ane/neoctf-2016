from datetime import date, timedelta as td

total = 0

# http://stackoverflow.com/a/7274316
d1 = date(2016, 1, 1)
d2 = date(2016, 12, 31)

delta = d2 - d1

def is_cube(n):
	x = int(round(n ** (1/3.0)))
	return x ** 3 == n

def is_square(n):
	x = int(round(n ** (1/2.0)))
	return x ** 2 == n

for i in range(delta.days + 1):
    day = d1 + td(days=i)
    day = str(day).replace("-", "")
    if day == "20161225":
        continue
    temp = sum(int(x) for x in day)
    if is_cube(temp) or is_square(temp):
        continue
    total += temp

print total
