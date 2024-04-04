def solution(word):

    words = []
    moeum = "AEIOU"
    
    def dfs(idx,word):
        
        if len(word) == 5:
            return
                     
        for i in range(5):
            words.append(word+moeum[i])
            dfs(i,word+moeum[i])
                    
    dfs(0,"")
    
    return words.index(word)+1