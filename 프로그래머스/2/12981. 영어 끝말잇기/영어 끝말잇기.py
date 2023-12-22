def solution(n, words):
    
    tmp = []    
    for i,word in enumerate(words):
        if not tmp:
            tmp.append(word)
            continue
        if word in tmp:
            return [i%n+1, i//n+1]
        else:
            if tmp[-1][-1] == word[0]:
                tmp.append(word)
            else:
                return [i%n+1, i//n+1]

    return [0,0]