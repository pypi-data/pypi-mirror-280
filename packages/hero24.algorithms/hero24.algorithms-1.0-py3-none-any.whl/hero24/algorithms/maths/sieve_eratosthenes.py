# Sieve of Eratosthenes

"""
   The greatest glory in living lies not in never falling,
       but in rising every time we fall.
         ~ Nelson Mandela
"""

class EratosthenesSieve:
    """
       Sieve of eratosthenes for generating set a set of prime numbers
    """
    def __init__(self, start, end, step=1):
        """
           start => number to start the prime range
           end => last number of prime range
           step => step inbetween range
        """
        self.set = {}
        self.change_sieve_properties(start, end, step)

    def get_last_set(self):
        """
           get last generated set
        """
        return self.set

    def change_sieve_properties(self, start, end, step=1):
        """
           change sieve properties
        """
        self.lst = [x for x in range(start, end, step)]
        self.step = step
        self.end = end
		
    def sieve(self):
        """
           run sieve with current config
        """
        number_set = set(self.lst)
        lst = [ x for x in range(2, self.end)]
        index = 0
        while index < len(self.lst):
            num = lst[index]
            tmp = 2
            while tmp < self.lst[len(self.lst)-1]:
                number_set.discard(num * tmp)
                tmp += 1
            index += 1
        self.set = number_set
        return self.get_last_set()
		

def eratosthenes_sieve(iterable):
        """
           Eratosthenes sieve function for iterables
        """
        iterable_set = set(iterable)
        mx = max(iterable)
        lst = [ x for x in range(2, mx)]
        for num in lst:
                tmp = 2
                while tmp < mx:
                        iterable_set.discard(num * tmp)
                        tmp += 1
        return iterable_set
