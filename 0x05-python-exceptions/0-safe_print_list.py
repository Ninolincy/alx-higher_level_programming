#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    num = 0
    try:
        for element in my_list:
            print(element, end='')
            num += 1
            if num == x:
                break
        print()
        return num
    except TypeError:
        return num
