import bisect


class OrderedList:

    def __init__(self):
        self._numbers = []

    def add(self, num):
        return bisect.insort(self._numbers, num)

    def __str__(self):
        return ', '.join(str(num) for num in self._numbers)


val = OrderedList()
print(val.add(5))
print(val.add(1))
print(val.add(52))
print(val.add(3))
print(val.add(32))
print(val)