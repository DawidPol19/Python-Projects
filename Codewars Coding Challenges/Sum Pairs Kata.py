# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 22:01:11 2019
Sum of Pairs
@author: Lofu
"""

l1= [1, 4, 8, 7, 3, 15]
import itertools
print(list(itertools.combinations(l1, 2)))

def combinations(iterable, r):
    # combinations('ABCD', 2) --> AB AC AD BC BD CD
    # combinations(range(4), 3) --> 012 013 023 123
    pool = tuple(iterable)
    n = len(pool)
    if r > n:
        return
    indices = range(r)
    yield tuple(pool[i] for i in indices)
    while True:
        for i in reversed(range(r)):
            if indices[i] != i + n - r:
                break
        else:
            return
        indices[i] += 1
        for j in range(i+1, r):
            indices[j] = indices[j-1] + 1
        yield tuple(pool[i] for i in indices)
print(list(combinations(l1, 2)))