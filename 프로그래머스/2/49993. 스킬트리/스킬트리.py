def solution(skill, skill_trees):
    
    prev = {skill[i]:i+1 for i in range(len(skill))}
    for i in range(len(skill_trees)):
        tmp = []
        for st in skill_trees[i]:
            if st in prev.keys():
                tmp.append(prev[st])
        skill_trees[i] = tmp
    
    answer = 0
    for skill_tree in skill_trees:
        start = 1
        flag = True
        for st in skill_tree:
            if start == st:
                start += 1
            else:
                flag = False
                break
        if flag:
            answer += 1
    
    return answer