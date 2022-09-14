"""
An array is called zero-plentiful if it contains multiple zeros, and every sequence of zeros is at least 4 items long.

Your task is to return the number of zero sequences if the given array is zero-plentiful, oherwise 0.

Examples

[0, 0, 0, 0, 0, 1]  -->  1
# 1 group of 5 zeros (>= 4), thus the result is 1

[0, 0, 0, 0, 1, 0, 0, 0, 0]  -->  2
# 2 group of 4 zeros (>= 4), thus the result is 2

[0, 0, 0, 0, 1, 0]  -->  0
# 1 group of 4 zeros and 1 group of 1 zero (< 4)
# _every_ sequence of zeros must be at least 4 long, thus the result is 0

[0, 0, 0, 1, 0, 0]  -->  0
# 1 group of 3 zeros (< 4) and 1 group of 2 zeros (< 4)

[1, 2, 3, 4, 5]  -->  0
# no zeros

[]  -->  0
# no zeros
"""


def zero_plentiful(arr):
    if 0 not in arr or arr.count(0) < 3:
        return 0
    elif arr.count(0) == len(arr):
        return 1
    else:
        counter = 0
        i = 0

        while i < len(arr):
            print(i, "i")
            if arr[i] == 0:
                if arr[i: i + 4].count(0) == 4:
                    counter += 1
                    if len(arr[i:]) == arr[i:].count(0):
                        return counter
                    else:
                        i += arr[i:].index(list(set(arr[i:]))[1])
                else:
                    return 0
            else:
                i += 1