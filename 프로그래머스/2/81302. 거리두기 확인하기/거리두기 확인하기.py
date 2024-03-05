from itertools import combinations

def solution(places):
    answer = []
    
    def manhattan_range(r1,c1,r2,c2):
        return abs(r1-r2) + abs(c1-c2)    
    
    for place in places:
        tmp = []
        for i in range(len(place)):
            for j in range(len(place[0])):
                if place[i][j] == "P":
                    tmp.append([i,j])
        
        flag = False
        for (r1,c1),(r2,c2) in combinations(tmp,2):            
            r = manhattan_range(r1,c1,r2,c2)
            if r > 2:
                continue
            elif r < 2:
                flag = True
                answer.append(0)
                break
            else:
                if r1 == r2:
                    if place[r1][(c1+c2)//2] == "O":
                        flag = True
                        answer.append(0)
                        break                            
                elif c1 == c2:
                    if place[(r1+r2)//2][c1] == "O":
                        flag = True
                        answer.append(0)
                        break                            
                else:
                    if place[r1][c2] == "O" or place[r2][c1] == "O":
                        flag = True
                        answer.append(0)
                        break

        if not flag:
            answer.append(1)
                
                    
    return answer
