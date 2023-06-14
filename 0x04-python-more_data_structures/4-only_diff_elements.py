#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    set_3 = set_2
    for x in set_1:
        if x in set_3:
            set_3.remove()
            continue
        set_3.add(x)
        return set_3
