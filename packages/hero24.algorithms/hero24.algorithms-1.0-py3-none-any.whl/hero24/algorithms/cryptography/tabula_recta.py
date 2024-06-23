from string import ascii_lowercase

# "I have no special talent I am only passionately curious"
# ~ Albert Einstein

def TabulaRecta():
    mat =[[l for l in ascii_lowercase[i:]] + [' '] +
          [l for l in ascii_lowercase[:i]]
           for i in range(len(ascii_lowercase)+1)
    ]
    def encrypt(text):
        s = ""
        for i in range(len(text)):
            s += mat[i%len(mat)][mat[0].index(text[i].lower())]
        return s

    def decrypt(text):
        s = ""
        for i in range(len(text)):
            s += mat[0][mat[i%len(mat)].index(text[i])]
        return s
    
    TabulaRecta.encrypt = encrypt
    TabulaRecta.decrypt = decrypt
    return TabulaRecta
