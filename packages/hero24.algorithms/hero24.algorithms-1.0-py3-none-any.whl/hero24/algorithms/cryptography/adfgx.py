from string import ascii_lowercase
from random import shuffle
from random import randint
from itertools import chain

"""  
    "Experience is the teacher of all things."
        ~ Julius Caesar 
"""


class ADFGX:
    """
        Implements a bit modified ADFGX cipher.
        - does not support numbers or special characters other than space
        - allows for multiple same letters in password
        - returns 36 character blocks padded if needed with underscores.
    """
    def __init__(self):
        letters = list(chain.from_iterable([
            ['_' for x in range(4)],
            [' '], list(ascii_lowercase),
            ['_' for x in range(5)]
            ]))
        shuffle(letters)
        mat = [[] for _ in range(6)]
        for idx in range(len(letters)):
            mat[idx%6].append(letters[idx])
        self._mat = mat
        self.letters = letters
        self._crypt = {"A":0,"D":1,"F":2,"G":3,"V":4,"X":5}


    def get_mat(self):
        """
           return polybius square matrix used for ciphering the message
        """
        return self._mat[:]


    def encrypt(self, word, passw):
        """
             encrypt the message using password.
             Does not support numbers or special characters.
        """
        crypt = []
        while not (len(word)*2)%36 == 0:
            word += "_"
        for c in word:                      
            idx = self.letters.index(c) % 6
            if c == "_":
                for i in range(randint(0,self.letters.count("_")-1)):
                    idx = self.letters[idx+1:].index(c)%6
            i = self._mat[idx].index(c)
            l = [None, None]
            for key in self._crypt:
                if self._crypt[key] == idx:
                    l[0] = key
                if self._crypt[key] == i:
                    l[1] = key
            for key in l:
                crypt.append(key)
        blocks = []
        for i in range(len(crypt)):
            if i % 6 == 0:
                blocks.append("".join(crypt[i:i+6]))
        crypt = [passw[:6]] + blocks
        for i in range(len(crypt)):
            crypt[i] = [c for c in crypt[i]]
        for i in range(len(crypt[0])-1, 0, -1):
            for j in range(i):
                if crypt[0][j] > crypt[0][j+1]:
                    for k in range(len(crypt)):
                        crypt[k][j], crypt[k][j+1] = crypt[k][j+1], crypt[k][j]
        for i in range(len(crypt)):
            crypt[i] = "".join(crypt[i])
        crypt.pop(0)
        return crypt


    def decrypt(self, ciphered, passwd):
        """
           decrypt previously encrypted message using given password
        """
        ciphered = ciphered[:]
        spasswd = [c for c in passwd[:6]]
        pmap = []
        s = ""
        for i in range(len(spasswd)-1, 0, -1):
            for j in range(i):
                if spasswd[j] > spasswd[j+1]:
                    pmap.append(j)
                    spasswd[j], spasswd[j+1] = spasswd[j+1], spasswd[j]
        for i in range(len(ciphered)):
            ciphered[i] = [c for c in ciphered[i]]
        pmap.reverse()
        for i in pmap:
            for block in ciphered:
                block[i], block[i+1] = block[i+1], block[i]
        for block in ciphered:
            idx = block
            for j in range(len(block)):
                if j % 2 == 0:
                    idx = block[j]
                else:
                    s+= self._mat[self._crypt[idx]][self._crypt[block[j]]]
        return s
