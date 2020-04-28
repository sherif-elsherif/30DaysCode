#!/bin/python3

# https://www.hackerrank.com/challenges/30-2d-arrays/problem

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))

counts = []
for i in range(4):
    for j in range(4):
        r1 = sum(arr[i][j:j+3])
        r2 = sum(arr[i+1][j+1:j+2])
        r3 = sum(arr[i+2][j:j+3])
        counts.append(r1 + r2 + r3)

counts = sorted(counts, reverse = True)
print(counts[0])
