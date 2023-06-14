#!/usr/bin/python3
def roman_to_int(roman_string):
    if roman_string is not str or roman_string is None:
        return 0
    roman_dictionary = {
        I: 1,
        V: 5,
        X: 10,
        L: 50,
        C: 100,
        D: 500,
        M: 1000,
    }
    decimalNum = ([roman_dictionary[n] for n in roman_string])
    output = 0
    for x in range(len(decimalNum)):
        output += decimalNum[x]

    return output
