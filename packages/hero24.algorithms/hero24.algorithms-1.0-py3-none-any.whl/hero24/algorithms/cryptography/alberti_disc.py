from string import ascii_uppercase
from string import ascii_lowercase
from random import shuffle
from random import randint

# "In the end, it is impossible not to become what others believe you are."
#     ~ Julius Caesar 

class AlbertiCommon:
    def __init__(self):
        self.outer_ring = [letter for letter in ascii_uppercase] + [' ']
        self.inner_ring = [letter for letter in ascii_lowercase] + [' ']
        self.initialize_inner_ring()
        self.block_size = 6

    def initialize_inner_ring(self):
        shuffle(self.inner_ring)
        self.reset_letter = self.inner_ring[0]

        
    def transform(self,start):
        while self.inner_ring[0] != start:
            l = self.inner_ring.pop(0)
            self.inner_ring.append(l)

            
class AlbertiLowerIndex(AlbertiCommon):
    def __init__(self):
        super().__init__()
        self.shift = 4

    def transform(self, index):
        idx = self.outer_ring[index]
        start = self.inner_ring[self.inner_ring.index(idx.lower())]
        super().transform(start)
        index += self.shift
        return idx, index
                
    def encrypt(self, text):
        super().transform(self.reset_letter)
        index , s = 0, ""
        for i in range(len(text)):
            if i % self.block_size == 0:
                idx, index = self.transform(index)
                s += idx
            s += self.inner_ring[self.outer_ring.index(text[i].upper())]
        return s

    def decrypt(self, text):
        s, index = "", 0
        super().transform(self.reset_letter)
        for i in range(len(text)):
            if text[i].isupper():
                _, index = self.transform(index)
            else:
                s += self.outer_ring[self.inner_ring.index(text[i])]
        return s


class AlbertiUpperIndex(AlbertiCommon):
    def __init__(self):
        super().__init__()
        self.outer_ring += ["1","2","3","4"]
        self.inner_ring += ["&","'",'"',"$"]
        self.initialize_inner_ring()

    def encrypt(self, text):
        s = ""
        self.transform(self.reset_letter)
        for i in range(len(text)):
            if i % self.block_size == 0:
                idx = self.outer_ring.index(str(randint(1,4)))
                s += self.outer_ring[idx]
                self.transform(self.inner_ring[idx])
            s += self.outer_ring[self.inner_ring.index(text[i].lower())]
        return s

    def decrypt(self, text):
        s = ""
        blocks = 0
        self.transform(self.reset_letter)
        for i in range(len(text)):
            if i % (self.block_size+blocks) == 0:
                idx = self.outer_ring.index(text[i])
                self.transform(self.inner_ring[idx])
                blocks = 1
                continue
            s += self.inner_ring[self.outer_ring.index(text[i].upper())]
        return s
