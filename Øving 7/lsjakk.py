#board = input("konge: k, dronning: q, tårn: r, løper: b, hest: n, og bonde: p, punktum: tomrom")
board = "kkkkkqqqqqrrrrrnnnnn"
def make_board(board_string):
    board = []
    for i in range(5):
        boardi = []
        for x in range(5):
            boardi.append(x)
        board.append(boardi)

    newlist = []
    x = 0
    while x < len(board):
        for i in board_string:
            newlist.append(i)
            if len(newlist) == 5:
                board[x] = newlist
                newlist = []
                x += 1


    return board


y =make_board(board)

#for i in y:
#    print(i)
#print(y)
