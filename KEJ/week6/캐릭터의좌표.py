def solution(keyinput, board):
    dic = {"left":(-1,0) , "right":(1,0), "up":(0,1), "down":(0,-1)}
    cht = [0,0]
    for i in keyinput:
        mv1 = cht[0] + dic[i][0]
        mv2 = cht[1] + dic[i][1]
        cht[0] = mv1 if abs(mv1) <= board[0]//2 else (mv1//abs(mv1)) * (board[0]//2)
        cht[1] = mv2 if abs(mv2) <= board[1]//2 else (mv2//abs(mv2)) * (board[1]//2)
    return cht