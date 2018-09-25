#!/usr/bin/env python3

#count number of swaps needed for bubble sort by comparing adjacent items and exchanging those that are out of order

import math
import os
import random
import re
import sys

def countSwaps(a):
    numSwaps = 0
    while True:
        swapsFlag = False
        for i in range(len(a)-1):
            if a[i] > a[i+1]:
                a[i], a[i+1] = a[i+1], a[i]
                numSwaps += 1
                swapsFlag = True
        if not swapsFlag:
            break
    print("Array is sorted in {} swaps.".format(numSwaps))
    print("First Element: {}".format(a[0]))
    print("Last Element: {}".format(a[-1]))

if __name__ == '__main__':
    n = int(input())

    a = list(map(int, input().rstrip().split()))

    countSwaps(a)
