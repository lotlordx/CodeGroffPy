def filter_positive_even_numbers(numbers):
    """Receives a list of numbers, and returns a filtered list of only the
       numbers that are both positive and even (divisible by 2), try to use a
       list comprehension."""
    filtered_number = [x for x in numbers if x % 2 == 0 and x > 0]
    return filtered_number


d1 = dict(mike=1, mary=3, joy=6)
d2 = dict(ayo=1, sam=30, emeka=19)
d3 = {**d1, **d2}
d4 = d1.update(d2)
print(d1)
print(d2)
print(d3)
print(d4)