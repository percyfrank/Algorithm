from collections import Counter

def solution(str1, str2):
    answer = 0
    
    def sets(str):
        tmp = []
        for i in range(len(str)-1):
            words = str[i:i+2]
            flag = True
            for word in words:
                if not word.isalpha():
                    flag = False
                    break
            if flag:
                tmp.append(words)
                
        return tmp
        
    word1,word2 = sets(str1.lower()),sets(str2.lower())
    A, B = Counter(word1) & Counter(word2), Counter(word1) | Counter(word2)
    cntA, cntB = sum(A.values()), sum(B.values())
    
    if cntB == 0:
        return 65536
    else:
        return int((cntA / cntB) * 65536)
    
