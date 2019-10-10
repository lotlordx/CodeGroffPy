from random import shuffle
from secrets import choice
from string import ascii_uppercase, digits

def gen_key(parts=3, chars_per_part=4):
    chars = [x for x in (ascii_uppercase + digits)]
    hello = choice(ascii_uppercase+digits)
    print(hello)
    seperator = "-"
    gen = ""
    while parts != 0:
        shuffle(chars)
        gen += "".join(chars[:chars_per_part]) + seperator
        parts -= 1
    return gen.rstrip("-")

print(gen_key(parts=100, chars_per_part=100))


from secrets import choice
from string import ascii_uppercase, digits

ALPHABET = ascii_uppercase + digits
DASH = '-'


def gen_key(parts=4, chars_per_part=8):
    return DASH.join(''.join(choice(ALPHABET) for i in range(chars_per_part))
                     for _ in range(parts))