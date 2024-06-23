# Sieve of Sundaram

"""
     The way to get started is to
          quit talking and begin doing.
        ~ Walt Disney
"""

def sundaram_sieve(iterable):
    """
        Sundaram sieve function for interables
    """
    numberset = set(iterable)
    stop = max(iterable)//2
    for i in range(1, stop):
        j = i
        f = i + j + (2 * i * j)
        while f <= stop:
            numberset.discard(f)
            j += 1
            f = i + j + (2 * i * j)
    num_list = []
    for n in numberset:
        num_list.append((2 * n) + 1)
    numberset.clear()
    for i in num_list:
        if i in iterable:
            numberset.add(i)
    return numberset
