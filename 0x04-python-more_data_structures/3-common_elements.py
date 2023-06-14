#!/usr/bin/python3
def common_elements(set_1, set_2):
    set_3 = set()
    for x in set_1:
        if x in set_2:
            set_3.add(x)
    return set_3
