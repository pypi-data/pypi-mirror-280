#!/bin/usr/env python3
# It is not our abilities that show what we truly are.  It is our choices
# ~ Albus Dumbledor @ Harry Potter and the Chamber of Secrets

def selection_sort(lst):
    " in place selection sort algorithm "
    for i in range(0,len(lst)-1):
        smallest = i
        for j in range(i,len(lst)):
            if lst[j] < lst[smallest]:
                smallest = j
        lst[i],lst[smallest] = lst[smallest],lst[i]

