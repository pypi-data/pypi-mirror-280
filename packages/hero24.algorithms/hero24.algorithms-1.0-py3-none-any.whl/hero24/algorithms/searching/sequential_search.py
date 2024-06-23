#!/bin/usr/env python3
# Happiness can be found even in the darkest of times, when one only remembers to turn on the light.
# ~ Albus Dumbledor @ Harry Potter and the Prizoner of Azkaban
def sequential_search(lst,target):
    "sequential search, return index of found item or None"
    for i in range(lst):
        if target == lst[i]:
            return i
