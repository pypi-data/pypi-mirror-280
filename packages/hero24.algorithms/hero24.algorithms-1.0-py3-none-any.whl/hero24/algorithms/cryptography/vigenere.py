from string import ascii_lowercase

# "Jobs fill your pocket but adventures fill your soul."
# ~ Jamie Lyn Beatty


def Vigenere():
    alpha = ascii_lowercase + ' '
    alpha = [[l for l in alpha[i:]] +
             [l for l in alpha[:i]]
             for i in range(len(alpha))
    ]
    
    def encrypt(key, text):
        s = ""
        for i in range(len(text)):
            index = alpha[0].index(key[i%len(key)])
            s += alpha[index][alpha[0].index(text[i].lower())]
        return s

    def decrypt(key, text):
        s = ""
        for i in range(len(text)):
            index = alpha[0].index(key[i%len(key)])
            s += alpha[0][alpha[index].index(text[i].lower())]
        return s

    Vigenere.encrypt = encrypt
    Vigenere.decrypt = decrypt
    return Vigenere


def VigenereAutokey():
    alpha = ascii_lowercase + ' '
    alpha = [[l for l in alpha[i:]] +
             [l for l in alpha[:i]]
             for i in range(len(alpha))
    ]
    
    def encrypt(key, text):
        # encrypt using plaintext for key
        s = alpha[alpha[0].index(key[0].lower())][alpha[0].index(text[0].lower())]
        for i in range(len(text[1:])):
            s += alpha[alpha[0].index(text[i].lower())][alpha[0].index(text[i+1].lower())]
        return s

    def decrypt(key, text):
        s = alpha[0][alpha[alpha[0].index(key[0].lower())].index(text[0].lower())]
        for i in range(len(text[1:])):
            s += alpha[0][alpha[alpha[0].index(s[i])].index(text[i+1].lower())]
        return s
    
    VigenereAutokey.encrypt = encrypt
    VigenereAutokey.decrypt = decrypt
    return VigenereAutokey


def VigenereAltAutokey():
    alpha = ascii_lowercase + ' '
    alpha = [[l for l in alpha[i:]] +
             [l for l in alpha[:i]]
             for i in range(len(alpha))
    ]
    
    def encrypt(key, text):
        # encrypt using plaintext for key
        s = alpha[alpha[0].index(key[0].lower())][alpha[0].index(text[0].lower())]
        for i in range(len(text[1:])):
            s += alpha[alpha[0].index(s[-1].lower())][alpha[0].index(text[i+1].lower())]
        return s

    def decrypt(key, text):
        s = alpha[0][alpha[alpha[0].index(key[0].lower())].index(text[0].lower())]
        for i in range(len(text[1:])):
            s += alpha[0][alpha[alpha[0].index(text[i])].index(text[i+1].lower())]
        return s
    
    VigenereAutokey.encrypt = encrypt
    VigenereAutokey.decrypt = decrypt
    return VigenereAutokey
