direct = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(-1,-1),(-1,1),(1,-1)]
def solution(board):
    maps = [[0]*len(board) for _ in range(len(board))]
    for idx1, val1 in enumerate(board):
        for idx2, val2 in enumerate(val1):
            if val2 ==1:
                maps[idx1][idx2] =1
                for d in direct:
                    nidx1, nidx2 = idx1+d[0], idx2+d[1]
                    if nidx1 in range(len(board)) and nidx2 in range(len(board)):
                        maps[nidx1][nidx2] = 1
    return sum(maps,[]).count(0)
