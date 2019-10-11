# from copy import deepcopy
#
# matrix1 = [[1, -2, 3], [-4, 5, -6], [7, -8, 9]]
# matrix2 = [[1, 1, 0], [1, -2, 3], [-2, 2, -2]]
#
#
# def add(array_one: list = matrix1, array_two: list = matrix2) -> list:
#     result = []
#     inner_result = []
#
#     for (first, second) in zip(array_one, array_two):
#         for nested_first, nested_second in zip(first, second):
#             if isinstance(nested_first, list) or isinstance(nested_second, list):
#                 inner_result.extend(add(nested_first,nested_second))
#             inner_result.append(nested_first + nested_second)
#         result.append(inner_result)
#         inner_result = []
#
#     return result


# def add(*args: list) -> list:
#
#     result = []
#     inner_result = []
#
#     def confirm_match(depth: tuple) -> None:
#         item_count = len(set([len(x) for x in first_depth]))
#         if item_count >= 2:
#             raise ValueError("Given matrices are not the same size.")
#
#     for first_depth in zip(*args):
#         confirm_match(first_depth)
#         for second_depth in zip(*first_depth):
#             confirm_match(second_depth)
#             inner_result.append(sum(second_depth))
#         result.append(inner_result)
#         inner_result = []
#
#     return result

from itertools import zip_longest


def add(*matrix):
    result = []
    for mats in zip_longest(*matrix):
        ans = []
        if None in mats:
            raise ValueError
        for item in zip_longest(*mats):
            if None in item:
                raise ValueError
            ans.append(sum(item))
        result.append(ans)
    return result



# print(add([[1, 9], [7, 3]], [[5, -4], [3, 3]], [[2, 3], [-3, 1]]))
# print(add(matrix1,matrix2))
#

m1 = [[6, 6], [3, 1]]
m2 = [[1, 2], [3, 4], [5, 6]]
m3 = [[6, 6], [3, 1, 2]]
print(add(m1, m2))