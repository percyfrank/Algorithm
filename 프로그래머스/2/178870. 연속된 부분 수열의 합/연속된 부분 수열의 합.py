def solution(sequence, k):
    
    prefix_sum = [0]
    for i in range(len(sequence)):
        prefix_sum.append(prefix_sum[-1]+sequence[i])    

    for i in range(1, len(sequence)+1):
        
        start = 0
        end = len(sequence) - i
        
        while start < end:
            mid = (start + end) // 2
            if prefix_sum[mid+i] - prefix_sum[mid] >= k:
                end = mid
            else:
                start = mid + 1
        
        if prefix_sum[start+i] - prefix_sum[start] == k:
            return [start, start+i-1]