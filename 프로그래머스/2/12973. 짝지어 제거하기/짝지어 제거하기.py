def solution(s):

    q = []
    for word in s:
        if not q:
            q.append(word)
        else:
            if q[-1] == word:
                q.pop()
            else:
                q.append(word)
    
    if not q:
        return 1
    else: 
        return 0
