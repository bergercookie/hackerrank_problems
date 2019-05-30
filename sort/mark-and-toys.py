#!/bin/python3

from typing import List
import math
import os
import random
import re
import sys

def merge_sort(l: list):
    # cornercase, 0 or 1 elements
    if len(l) <= 1:
        return l

    left = l[:len(l)//2]
    right = l[len(l)//2:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left: list, right: list):
    result: List[int] = []
    
    while left and right:
        if left[0] <= right[0]:
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))

    if left:
        result.extend(left)
    elif right:
        result.extend(right)
    else:
        raise RuntimeError("Not gonna happen")
    
    return result

# Complete the maximumToys function below.
def maximumToys(prices, k):
    prices_sorted = merge_sort(prices)

    s = 0
    i = 0
    num_toys = 0
    while i < len(prices_sorted):
        s += prices_sorted[i]
        if s > k:
            break

        num_toys += 1
        i += 1

    return num_toys


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nk = input().split()
    n = int(nk[0])
    k = int(nk[1])

    prices = list(map(int, input().rstrip().split()))
    result = maximumToys(prices, k)
    fptr.write(str(result) + '\n')
    fptr.close()

