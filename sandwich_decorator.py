import re
from collections import ChainMap, Counter
from functools import wraps

UPPER_SLICE = "=== Upper bread slice ==="
LOWER_SLICE = "=== Lower bread slice ==="


def sandwich(func):
    """Write a decorator that prints UPPER_SLICE and
       LOWER_SLICE before and after calling the function (func)
       that is passed in  (@wraps is to preserve the original
       func's docstring)
    """

    @wraps(func)
    def wrapped(*args, **kwargs):
        print(UPPER_SLICE)
        result = (func(*args, **kwargs))
        print(LOWER_SLICE)

        return result

    return wrapped


baseline = {'music': 'bach', 'art': 'rembrandt'}
adjustments = {'art': 'van gogh', 'opera': 'carmen'}
# print(ChainMap(adjustments, baseline))


words = re.findall(r'\w+', open('add.txt').read().lower())
print(words)
vals = Counter(words).most_common(5)
print(vals)
