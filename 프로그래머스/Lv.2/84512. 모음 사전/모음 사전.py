def solution(word):

    words = []
    moeum = "AEIOU"

    def dfs(idx,w):
        if idx == 5:
            return
        
        for i in range(len(moeum)):
            words.append(w+moeum[i])
            dfs(idx+1,w+moeum[i])
                    
    dfs(0,"")

    return words.index(word)+1
    