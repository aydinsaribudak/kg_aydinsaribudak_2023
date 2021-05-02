#import numpy as np



a = [34, 2, 467]

for i in range(len(a)):

    remainder = []
    
    # calcute remainder and quotient
    rem = a[i] % 10
    remainder.append(rem)
    quot = int(a[i] / 10)
    #print(quot)

    # calcute remainder and quotient recursively
    while quot >= 1:
        rem = quot % 10
        remainder.append(rem)
        quot = int(quot / 10)
        print(quot)

    print(remainder)




