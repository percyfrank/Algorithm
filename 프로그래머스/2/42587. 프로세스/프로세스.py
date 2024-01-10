def solution(priorities, location):
    
    queue = [[idx,priority] for idx,priority in enumerate(priorities)]
    answer = 0  
    while queue:
        idx,priority = queue.pop(0)
        
        if any(priority < q[1] for q in queue):
            queue.append((idx,priority))
        else:
            answer += 1
            if idx == location:
                return answer
    
    
  