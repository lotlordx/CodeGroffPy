

def get_index_different_char(chars):
    start_list = [0]*len(chars)
    is_alnum, is_not_alum = 1, 0

    for key, char in enumerate(chars):
        if str(char).isalnum():
            start_list[key] = is_alnum
        else:
            start_list[key] = is_not_alum
    is_alnum_count , is_not_alum_count = start_list.count(is_alnum), start_list.count(is_not_alum)

    if is_alnum_count > is_not_alum_count:
        return start_list.index(is_not_alum)
    else:
        return start_list.index(is_alnum)


num = ['.', '{', '.', 'Q', '+']


print(get_index_different_char(num))