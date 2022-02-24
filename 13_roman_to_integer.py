from re import sub


# First try
def romanToInt(s: str) -> int:
    conversion = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    conversion_with_sub = {
        "IV": 4,
        "IX": 9,
        "XL": 40,
        "XC": 90,
        "CD": 400,
        "CM": 900,
    }

    sub_keys = conversion_with_sub.keys()

    converted_int = 0

    while any(substring in s for substring in sub_keys):
        for substring in sub_keys:
            if substring in s:
                print(substring)
                s = s.replace(substring, "")
                converted_int += conversion_with_sub[substring]

    for numeral in s:
        converted_int += conversion[numeral]

    return converted_int


# print(romanToInt("MCMXCIV"))


# Faster attempt


def roman_to_int(s):
    conversion = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000,
    }

    cool_int = 0

    while s:

        if len(s) >= 2:
            test = s[0] + s[1]
            if test == "IV" or test == "IX":
                cool_int -= 1
                s = s[1:]
            elif test == "XL" or test == "XC":
                cool_int -= 10
                s = s[1:]
            elif test == "CD" or test == "CM":
                cool_int -= 100
                s = s[1:]

        cool_int += conversion[s[0]]
        s = s[1:]

    return cool_int


print(roman_to_int("MCMXCIV"))
