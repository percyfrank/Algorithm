from collections import deque

def solution(s):
    answer = 0
    
    q = deque(s)    
    for _ in range(len(s)):
        stack = []   
        for i in q:
            if stack:
                if stack[-1] == "(" and i == ")":
                    stack.pop()
                elif stack[-1] == "{" and i == "}":
                    stack.pop()
                elif stack[-1] == "[" and i == "]":
                    stack.pop()
                else:
                    stack.append(i)
            else:
                stack.append(i)
                
        if not stack:
            answer += 1
            
        q.rotate(-1)
        
    return answer