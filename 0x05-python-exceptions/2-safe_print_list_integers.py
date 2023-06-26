#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    try:
        num = 0
        for elements in my_list[:x]:
            try:
                print("{:d}".format(elements), end='')
                num += 1
            except (ValueError, TypeError):
                continue
        print()
        return num
    except TypeError:
        return num
