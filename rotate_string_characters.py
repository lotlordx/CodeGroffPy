from collections import deque


def rotate(string, n):
    """Rotate characters in a string.
       Expects string and n (int) for number of characters to move.
    """
    deque_string = deque(string)
    deque_string.rotate(-n)
    return ''.join(deque_string)

print(rotate('hello', 2))
