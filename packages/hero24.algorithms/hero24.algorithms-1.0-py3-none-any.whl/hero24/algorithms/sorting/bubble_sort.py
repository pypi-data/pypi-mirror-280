#!/bin/usr/env python3
#  We must all face the choice between what is right and what is easy.
#  ~ Albus Dumbledore @ Harry Potter and the Gobblet of Fire.
def bubble_sort(lst):
    "in place implementation of bubble sort"
    for i in range(len(lst)-1,0,-1):
        for j in range(0,i):
            if lst[j] > lst[j+1]:
                lst[j],lst[j+1] = lst[j+1],lst[j]
