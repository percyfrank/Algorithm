l,c = map(int,input().split())
words = list(input().split())
words.sort()
visited = [False] * c

def backtracking(idx, cnt, word):
    
    if cnt == l:
        vowel = 0
        conso = l
        for w in word:
            if w in ['a', 'e', 'i', 'o', 'u']:
                vowel += 1
                conso -= 1
        if vowel >= 1 and conso >= 2:
            print("".join(word))
        return
    
    for i in range(idx, c):
        if not visited[i]:
            visited[i] = True
            backtracking(i + 1, cnt + 1, word + words[i])
            visited[i] = False
            
backtracking(0, 0, "")

    