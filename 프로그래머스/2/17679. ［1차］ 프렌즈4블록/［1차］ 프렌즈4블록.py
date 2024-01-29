def solution(m, n, board):
    
    for i in range(m):
        board[i] = list(board[i])
    
    tmp = set()
    answer = 0
    while True:
        
        for i in range(m-1):
            for j in range(n-1):
                t = board[i][j]
                if t == board[i+1][j] == board[i][j+1] == board[i+1][j+1] != "":
                    tmp.add((i,j))
                    tmp.add((i+1,j))
                    tmp.add((i,j+1))
                    tmp.add((i+1,j+1))
            
        if tmp:
            answer += len(tmp)
            for i,j in tmp:
                board[i][j] = ""
            tmp = set()
        else:
            return answer
        
        # 바닥까지 밀어주기
        while True:
            flag = True
            for i in range(m-1):
                for j in range(n):
                    if board[i][j] and board[i+1][j] == "":
                        board[i+1][j] = board[i][j]
                        board[i][j] = ""
                        flag = False
            # 바닥까지 밀어줄 블록이 없을 경우 중지
            if flag:
                break
