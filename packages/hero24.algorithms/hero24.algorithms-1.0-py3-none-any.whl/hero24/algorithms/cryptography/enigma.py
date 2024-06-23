from string import ascii_uppercase

# "THERE IS NOTHING SAFER THAN FLYING, IT’S CRASHING THAT IS DANGEROUS"
# ~ THEO COWAN

class Ring():
    def __init__(self, start='A'):
        ring = [l for l in ascii_uppercase]
        self.idxring = ring[ring.index(start):] + ring[:ring.index(start)]
        ring = self.idxring[::]
        for i in range(len(ring)//2):
            ring[-i], ring[i] = ring[i], ring[-i]
        self.ring = ring
        self.shifts = 0
        
    def __getitem__(self, key):
            val = self.ring[self.idxring.index(key)]
            return val

    def __len__(self):
        return len(self.ring)

    def shift(self):
        self.ring.append(self.ring.pop(0))
        self.shifts += 1


class Plugboard:
    def __init__(self, swaps):
        self.board = {l:l for l in ascii_uppercase}
        for key in swaps:
            self.board[key.upper()] = swaps[key]
            self.board[swaps[key]] = key.upper()

    def __getitem__(self, key):
        return self.board[key]


class Enigma:
    def __init__(self, ringpositions=["A","B","C"], plugswaps={}):
        self.rpos = ringpositions
        self.reset()
        self.reflector = Ring()
        self.plugboard = Plugboard(plugswaps)

    def reset(self):
        ra, rb, rc = self.rpos
        self.fring = Ring(ra)
        self.sring = Ring(rb)
        self.tring = Ring(rc)

    def _shift(self, ring, nring):
        if ring.shifts % len(ring) == 0:
                nring.shift()

    def encrypt(self,text):
        text = text.upper().replace(' ','X')
        s = ""
        for i in text:
            i = self.plugboard[i]
            initpass = self.reflector[self.tring[self.sring[self.fring[i]]]]
            s += self.plugboard[self.fring[self.sring[self.tring[initpass]]]]
            self.fring.shift()
            self._shift(self.fring, self.sring)
            self._shift(self.sring, self.tring)
        return s

