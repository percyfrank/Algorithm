from heapq import heappop,heappush

def solution(book_time):

    book_time.sort()
    for idx,time in enumerate(book_time):
        start = int(time[0][:2]) * 60 + int(time[0][3:])
        end = int(time[1][:2]) * 60 + int(time[1][3:]) 
        book_time[idx] = [start,end+10]

    rooms = []
    for time in book_time:
        if len(rooms) != 0 and rooms[0] <= time[0]:
            heappop(rooms)
        heappush(rooms,time[1])
        
    return len(rooms)