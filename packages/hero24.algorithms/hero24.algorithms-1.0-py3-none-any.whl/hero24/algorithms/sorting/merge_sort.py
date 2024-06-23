#!/usr/bin/env python3
# You're a Timex watch in a digital age.
# ~ Thomas Gabriel @ Die Hard 4.0

def merge_(lst_a,lst_b):
    ' merging function '
    result = []
    right = 0
    left = 0
    length = len(lst_a) if len(lst_a) > len(lst_b) else len(lst_b)
    for i in range(length):
        if lst_a[right] <= lst_b[left]:
            result.append(lst_a[right])
            right += 1
        else:
            result.append(lst_b[left])
            left += 1
    result += lst_a[right:]
    result += lst_b[left:]
    return result
    

def merge_sort(lst):
    ' out-of-place implementation of merge sort'
    if len(lst) > 1:
        return merge_(merge_sort(lst[:len(lst)//2]),merge_sort(lst[len(lst)//2:]))
    else:
        return lst
