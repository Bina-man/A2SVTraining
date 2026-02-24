#!/bin/python3

import math
import os
import random
import re
import sys


def countSwaps(a):
    total_couted_swaps = 0
    for index, val in enumerate(a):
        internal_counter = index
        while  internal_counter > 0:
            if val < a[internal_counter-1]:
                a[internal_counter-1], a[internal_counter] = a[internal_counter], a[internal_counter-1]
                total_couted_swaps +=1
            internal_counter -=1
    print(f"Array is sorted in {total_couted_swaps} swaps.")
    print(f"First Element: {a[0]}")
    print(f"Last Element: {a[len(a)-1]}")

if __name__ == '__main__':
    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))
    
    countSwaps(a)
