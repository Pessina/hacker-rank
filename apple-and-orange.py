#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the countApplesAndOranges function below.
def countApplesAndOranges(s, t, a, b, apples, oranges):
    for i in range(0, len(apples)):
        apples[i] = apples[i] + a

    count = 0
    for i in apples:
        if (i >= s and i <=t):
            count += 1
    print (count)

    for i in range(0, len(oranges)):
        oranges[i] = oranges[i] + b
    
    count = 0
    for i in oranges:
        if (i >= s and i <=t):
            count += 1
    print (count)


    
if __name__ == '__main__':
    st = input().split()

    s = int(st[0])

    t = int(st[1])

    ab = input().split()

    a = int(ab[0])

    b = int(ab[1])

    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)

