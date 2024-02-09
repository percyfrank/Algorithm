# def solution(sequence, k):
#     answer = []
    
#     prefix_sum = [0]
#     for i in range(len(sequence)):
#         prefix_sum.append(prefix_sum[-1]+sequence[i])
    
    

#     for i in range(1,len(sequence)+1):
        
#         start = 0
#         end = len(sequence)-i
        
#         while start <= end:
#             mid = (start + end) // 2
#             print(mid)
#             # if sequence[mid+i] - sequence[mid] == k:
#             #     return [start, start+i-1]
#             elif sequence[mid+i] - sequence[mid] >= k:
#                 end = mid
#             else:
#                 start = mid + 1
                
#         if sequence[mid+i] - sequence[mid] == k:
#             return [start, start+i-1]
#             
    # return answer
    
def solution(sequence, k):
    L = len(sequence)
    sequence = [0] + sequence

    for i in range(1, L+1):
        sequence[i] = sequence[i-1] + sequence[i]

    for l in range(1, L + 1):

        s = 0
        e = L - l

        while s < e:
            m = (s + e) // 2
            if sequence[m+l] - sequence[m] >= k:
                e = m
            else:
                s = m + 1

        if sequence[s+l] - sequence[s] == k:
            return [s, s + l - 1]