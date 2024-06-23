from string import ascii_lowercase

"""
    "Without training, they lacked knowledge.
     Without knowledge, they lacked confidence.
     Without confidence, they lacked victory."
          ~ Julius Caesar 
"""

class Caesar:
    def __init__(self, shift):
        self.alphabet = ascii_lowercase + " "
        self.shifted = self.alphabet[shift:] + self.alphabet[:shift]

    def encrypt(self, text):
        s = ""
        for c in text:
            s += self.shifted[self.alphabet.index(c)]
        return s

    def decrypt(self, text):
        s = ""
        for c in text:
            s += self.alphabet[self.shifted.index(c)]
        return s


class ROT13(Caesar):
    def __init__(self):
        super().__init__(13)
