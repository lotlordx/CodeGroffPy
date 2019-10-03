def divide_numbers(numerator, denominator):
    """For this exercise you can assume numerator and denominator are of type
       int/str/float.
       Try to convert numerator and denominator to int types, if that raises a
       ValueError reraise it. Following do the division and return the result.
       However if denominator is 0 catch the corresponding exception Python
       throws (cannot divide by 0), and return 0"""
    try:
        num = int(numerator)
        dim = int(denominator)
        try:
            division = num / dim
            return division
        except:
            return ZeroDivisionError('division by zeros')
    except:
        raise ValueError("Values passed can't be converted to an interger")


print(divide_numbers(4, 0))