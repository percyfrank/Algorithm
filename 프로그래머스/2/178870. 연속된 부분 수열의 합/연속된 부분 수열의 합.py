def solution(sequence, k):
    
    prefix_sum = [0]
    for i in range(len(sequence)):
        prefix_sum.append(prefix_sum[-1] + sequence[i])
    # print(prefix_sum)
    
    answer = []
    for i in range(1,len(sequence)+1):
        
        left = 0
        right = len(sequence)-i
        
        while left < right:
            mid = (left + right) // 2
            if prefix_sum[mid+i] - prefix_sum[mid] >= k:
                right = mid
            else:
                left = mid + 1
                
        
        if prefix_sum[left+i] - prefix_sum[left] == k:
            return [left,left+i-1]
            
    
    
    return answer