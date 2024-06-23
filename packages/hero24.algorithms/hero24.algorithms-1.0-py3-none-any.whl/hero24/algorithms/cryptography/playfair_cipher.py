from string import ascii_lowercase

"""
    "DON’T WORRY ABOUT THE WORLD ENDING TODAY, 
	IT’S ALREADY TOMORROW IN AUSTRALIA." 
	~ CHARLES M. SCHULZ
"""

class PlayfairCipher():
    def __init__(self, key=None):
        self.mat = [[]]
        if key:
            alpha = key
        else:
            alpha = ""
        alpha = alpha + ascii_lowercase + ' ' + '0' + '_' + ','
        for j in range(36):
            for k in range(len(self.mat)):
                if not alpha:
                    break
                if alpha[0] in self.mat[k]:
                    alpha = alpha[1:]
                    break
            else:
                if len(self.mat[-1]) > 5:
                    self.mat.append([])
                self.mat[-1].append(alpha[0])
                alpha = alpha[1:]


    def __rc_check(self, ctl, ptl):
        ialph, jalph = None, None
        for j in range(len(self.mat)):
            if ctl in self.mat[j]:
                jalph = self.mat[j]
            if ptl in self.mat[j]:
                ialph = self.mat[j]
            if ialph and jalph:
                return ialph, jalph


    def __it_pad(self, text):
        while len(text) % 2 != 0:
            text += ' '
        return text.lower()
            

    def encrypt(self, text):
        s, text = '', self.__it_pad(text)
        for i in range(1,len(text), 2):
            ialph, jalph = self.__rc_check(text[i], text[i-1])
            if ialph is jalph:
                # same row
                s += ialph[(ialph.index(text[i-1])+1)%len(ialph)]
                s += jalph[(jalph.index(text[i])+1)%len(jalph)]
            elif jalph.index(text[i]) == ialph.index(text[i-1]):
                # same column
                jdx, idx = self.mat.index(jalph), self.mat.index(ialph)
                s += self.mat[(idx+1)%len(self.mat)][ialph.index(text[i-1])]
                s += self.mat[(jdx+1)%len(self.mat)][jalph.index(text[i])]
            else:
                s += jalph[(ialph.index(text[i-1])+1)%len(ialph)]
                s += ialph[(jalph.index(text[i])+1)%len(jalph)]
        return s


    def decrypt(self, text):
        s, text = "", text.lower()
        for i in range(1, len(text), 2):
            ialph, jalph = self.__rc_check(text[i], text[i-1])
            if ialph is jalph:
                s += ialph[ialph.index(text[i-1])-1]
                s += jalph[jalph.index(text[i])-1]
            elif jalph.index(text[i]) == ialph.index(text[i-1]):
                jdx, idx = self.mat.index(jalph), self.mat.index(ialph)
                s += self.mat[idx-1][ialph.index(text[i-1])]
                s += self.mat[jdx-1][jalph.index(text[i])]
            else:
                s += jalph[ialph.index(text[i-1])-1]
                s += ialph[jalph.index(text[i])-1]
        return s
