def search_replace(my_list, search, replace):
    newList = my_list.copy()
    idx_list = [index for index, el in enumerate(my_list) if el == search]
    for idx in idx_list:
        newList[idx] = replace
    return newList
