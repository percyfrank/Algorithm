def solution(board):
    
    answer = 0
    for i in range(1,len(board)):
        for j in range(1,len(board[0])):
            if board[i][j] == 1:
                board[i][j] = min(board[i-1][j],board[i][j-1],board[i-1][j-1]) + 1    
                
    for i in range(len(board)):
        for j in range(len(board[i])):
            answer = max(answer,board[i][j])
    
    return answer**2