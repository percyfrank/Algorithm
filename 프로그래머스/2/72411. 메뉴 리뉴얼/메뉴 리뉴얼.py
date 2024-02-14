from itertools import combinations
from collections import Counter
 
def solution(orders, course):
    
    answer = []
    for c in course:
        tmp = []
        for order in orders:
            tmp += combinations(sorted(order),c)
        
        tmp = Counter(tmp).most_common()
        answer += [key for key,value in tmp if value > 1 and value == tmp[0][1]]
        
    return [''.join(data) for data in sorted(answer)]