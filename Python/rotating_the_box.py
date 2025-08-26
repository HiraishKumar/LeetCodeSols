arr =   [["#","#","*",".","*","."],
        ["#","#","#","*",".","."],
        ["#","#","#",".","#","."]]

def Rotate(box:list[list[int]])->list[list[int]]:

    row , col = len(box),len(box[0])
    res = [["."]*row for _ in range(col)]

    for r in range(row):
        i = col - 1
        for c in reversed(range(col)):
            if box[r][c] == "#":
                res[i][row - r - 1] = "#"
                i -= 1
            if box[r][c] == "*":
                res[c][row - r - 1] = "*"
                i = c - 1
    for k in box:
        print(k)
    for i in res:
        print(i)

    return res

Rotate(arr)

    #trans position (half)
    # m = len(box)
    # n = len(box[0])

    # res = [["." for i in range(m)] for j in range(n)]
    # for row in range(m):
    #     stoneInRow_count = 0
    #     for cell in range(n):
    #         if box[row][cell] == "#":
    #             stoneInRow_count += 1
    #         elif box[row][cell] == "*":
    #             res[cell][m-row-1] = "*"
    #             res_row = cell
    #             res_col = row
    #             while stoneInRow_count > 0:
    #                 res[res_row][res_col] = "#"
    #                 res_row -= 1
    #                 stoneInRow_count -= 1
    #             stoneInRow_count = 0
    #         elif cell == m-1:
    #             res_row = cell
    #             res_col = row
    #             while stoneInRow_count > 0:
    #                 res[res_row][res_col] = "#"
    #                 res_row -= 1
    #                 stoneInRow_count -= 1
    #             stoneInRow_count = 0