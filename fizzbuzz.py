

def fizzbuzz(num: int) -> str or int:
    fizz, buzz = 'Fizz', 'Buzz'

    if num % 3 == 0 and num % 5 == 0:
        print(f"{fizz} {buzz}")
    elif num % 3 == 0:
        print(fizz)
    elif num % 5 == 0:
        print(buzz)
    else:
        print(num)
fizzbuzz(100)