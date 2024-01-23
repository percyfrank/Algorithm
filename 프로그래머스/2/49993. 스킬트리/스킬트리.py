def solution(skill, skill_trees):
    
    answer = 0
    for skill_tree in skill_trees:
        tmp = ''
        for st in skill_tree:
            if st in skill:
                tmp += st
        
        if tmp == skill[0:len(tmp)]:
            answer += 1
    
    return answer