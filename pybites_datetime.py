from datetime import datetime, timedelta
from itertools import islice

PYBITES_BORN = datetime(year=2016, month=12, day=19)


def gen_special_pybites_dates():
    days = 0
    while True:
        days += 1
        if days % 100 == 0 or days % 365 == 0:
            yield PYBITES_BORN + timedelta(days=days)

date = gen_special_pybites_dates()
dates = list(islice(date, 10))

# print(dates)
print(dates)
# print(next(date))
# print(next(date))
# print(next(date))
# print(next(date))
# print(next(date))
# print(next(date))
# print(next(date))
# print(next(date))
# print(next(date))