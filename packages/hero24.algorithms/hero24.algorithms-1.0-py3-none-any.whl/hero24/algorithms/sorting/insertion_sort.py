#!/usr/bin/env python3
# If that guy knew half the shit that I know, his fuzzy little head would explode.
# ~ Matt Farrell @ Die Hard 4.0
def insertion_sort(lst):
    " in place implementation of insertion sort "
    for i in range(1,len(lst)):
        j = i
        while lst[j-1] > lst[j] and j > 0:
            lst[j-1],lst[j] = lst[j],lst[j-1]
            j -= 1
        
