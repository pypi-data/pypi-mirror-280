"""
Module containing different implementations of 
fibonacci sequence demonstarting different
programming techniques.
"""

# "Są trzy gatunki kłamstwa: 1) kłamstwo pospolite,
# 2) przysięga, 3) statystyka" ~ Julian Tuwim


def fibonacci_recursive(n):
    """
        recursive implementation of fibonacci
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci_recursive(n-1) + fibonacci_recursive(n-2)


def fibonacci_iterative(n):
    """
       non-recursive implementation of fibonacci
    """
    seq = [0,1]
    nxt = seq[0]
    count = 1
    while count <= n:
        count += 1
        seq = seq[1], nxt
        nxt = seq[0] + seq[1]
    return nxt


def fibonacci_memo(n, mem=[0,1]):
    """
       recursive fibonacci sequence using
       memoization.
    """
    if n >= len(mem):
        mem.append(fibonacci_memo(n-1) + fibonacci_memo(n-2))
    return mem[n]


def fibonacci_dynamic(n, dyn=None):
    """
       iterative fibonacci sequence done
       using dynamic programming
    """
    if dyn is None:
        dyn = [0,1]
    for i in range(len(dyn),n+1):
        dyn.append(dyn[i-1] + dyn[i-2])
    return dyn[n], dyn

