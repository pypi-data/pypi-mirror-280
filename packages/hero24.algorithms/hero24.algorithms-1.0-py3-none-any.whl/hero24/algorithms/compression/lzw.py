#!/usr/bin/env python3
# "There is nothing premanent except change" ~ Heraclitus

class BadCompressionError(Exception):
    pass

class LZW:
    @staticmethod
    def compress(uncompressed):
        hashmap = {chr(i): i for i in range(256)}
        w = ""
        result = []
        for c in uncompressed:
            wc = w + c
            if wc in hashmap:
                w = wc
            else:
                result.append(hashmap[w])
                hashmap[wc] = len(hashmap) 
                w = c
        if w:
            result.append(hashmap[w])
        return result
    
    @staticmethod
    def decompress(compressed):
        hashmap = {i:chr(i) for i in range(256)}
        w = chr(compressed[0])
        result = w
        for i in compressed[1:]:
            if i in hashmap:
                entry = hashmap[i]
            elif i == len(hashmap):
               entry = w + w[0]
            else:
                raise BadCompressionError("Corrupted data")
            result += entry
            hashmap[len(hashmap)] = w + entry[0]
            w = entry
        return result

