import time


def time_it(func: object):

    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"it took {func.__name__} {(end - start) * 1000} mil secs")

        return result
    return wrapper


@time_it
def cal_sqr(num: list) -> list:
    result = []
    for i in num:
        result.append(i*i)
    return result


@time_it
def cal_cube(num: list) -> list:
    result = []
    for i in num:
        result.append(i*i*i)
    return result


array_elements = [1,3,5,7,8,9]
print(cal_sqr(array_elements))
print(cal_cube(array_elements))
