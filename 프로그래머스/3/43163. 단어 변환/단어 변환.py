def solution(begin, target, words):
        
    def compare(a,b):
        
        cnt = 0   
        for i in range(len(begin)):
            if a[i] != b[i]:
                cnt += 1
        
        return True if cnt == 1 else False
    
    def dfs(word,cnt):
            
        if word == target:
            cnt_list.append(cnt)
            return
        
        for i in range(len(words)):
            if not visited[i] and compare(word,words[i]):
                visited[i] = True
                dfs(words[i],cnt+1)
                visited[i] = False
        

    visited = [False] * len(words)
    cnt_list = []
    dfs(begin,0)
        
    return min(cnt_list) if cnt_list else 0