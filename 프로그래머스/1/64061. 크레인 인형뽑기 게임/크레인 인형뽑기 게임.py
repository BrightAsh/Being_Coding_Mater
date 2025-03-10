def solution(board, moves):
    backet = []
    tmp = -1
    answer = 0
    for move in moves:
        for i in range(len(board)):
            if board[i][move-1] != 0:
                backet.append(board[i][move-1])
                board[i][move-1] = 0
                tmp +=1
                while len(backet) >=2 and backet[tmp] == backet[tmp-1]:
                    backet = backet[:-2] if len(backet) > 2 else []
                    tmp -= 2
                    answer+=1
                break;
    return answer*2