def replace(list: list, begin: int, end: int, newlist: list) -> list:
    """
    replaces elements between the given indexes

    Parameters
    ----------
    list: the list to modify (list)
    begin: the starting index of the replacement (int)
    end: the ending index of the replacement (int)
    newlist: the list of elements to put in the original list (list)

    Returns
    -------
    list: the modified list

    Notes
    -----
    Negative indexes are not supported.
    If the given indexes are not valid then the function returns None.
    """

    index_newlist = 0

    if end < begin:
        return None

    if begin < 0 or end > (len(list) - 1):
        return None


    for index_list in range(begin, end + 1):

        if index_newlist > len(newlist) - 1:
            index_newlist = 0

        list[index_list] = newlist[index_newlist]
        index_newlist += 1

    return list

test = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
newtest = [0, 1, 2, 3]

print(replace(test, 2, 9, newtest))