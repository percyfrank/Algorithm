from itertools import product

def solution(word):

    words = []
    for i in range(1,6):
        for data in product("AEIOU",repeat=i):
            words.append(''.join(data))
    words.sort()

    return words.index(word)+1
    