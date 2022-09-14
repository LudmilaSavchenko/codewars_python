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


"""
#var 1

def zero_plentiful(arr):
    if 0 not in arr or arr.count(0) < 3:
        return 0
    else:
        counter = 0
        i = 0
        while i < len(arr):
            if arr[i] == 0:
                if arr[i: i + 4].count(0) == 4:
                    if len(set(arr[i:])) == 1: len0 = len(arr[i:])
                    else: len0 = arr[i:].index(list(set(arr[i:]))[1])
                    counter += len0 // 4
                    i += len0
                else:
                    return 0
            else:
                i += 1
        return counter
"""

def zero_plentiful(a):
    z = [len(w) for w in ''.join('0' if not e else ' ' for e in a).strip().split()]
    return len(z) if z and min(z) >= 4 else 0