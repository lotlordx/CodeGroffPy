



def flatten(list_of_lists):

    new_list = []

    for item in list_of_lists:
        if isinstance(item, list) or isinstance(item, tuple):
            new_list.extend(flatten(item))
        else:
            new_list.append(item)

    return new_list


list_val = [1, 2, [3, 4], [5, [6, 7]], [8, [9, [10]]], [11, [12, 13], [14, [15, 16, [17, 18, [19, 20]]]]]]
list_val = [1, (2, 3), [(4, 5), [6, 7, [8, 9, 10]]]]


print((flatten(list_val)))

def test_works_with_tuple_as_well():
    inp = [1, (2, 3), [(4, 5), [6, 7, [8, 9, 10]]]]
    print(flatten(inp))
    expected = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    assert list(flatten(inp)) == expected


def test_flatten_ints_and_chars():
    inp = ['a', 'b', [1, 2, 3],
           ['c', 'd', ['e', 'f', ['g', 'h']]],
           [4, [5, 6, [7, [8]]]]]
    print(flatten(inp))
    expected = ['a', 'b', 1, 2, 3, 'c', 'd', 'e', 'f', 'g',
                'h', 4, 5, 6, 7, 8]
    assert list(flatten(inp)) == expected

# test_flatten_ints_and_chars()

test_works_with_tuple_as_well()