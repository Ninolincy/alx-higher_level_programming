#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    sum = 0
    num = sys.argv
    if len(num) > 1:
        for number in range(1, len(num)):
            sum += int(num[number])
    print("{:d}".format(sum))
