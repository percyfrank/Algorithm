def solution(book_time):
    
    visited = [0] * 1450
    
    for time in book_time:
        start_h,start_m = map(int,time[0].split(":"))
        end_h,end_m = map(int,time[1].split(":"))
        start = start_h * 60 + start_m
        end = end_h * 60 + end_m + 10
        for i in range(start,end):
            visited[i] += 1

    print(visited)
    
    return max(visited)
                            
