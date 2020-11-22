turn = True
#Defines that nobody has won at the start of the game
winVal = True
#Creates the board to play on
board = [[0,0,0],
        [0,0,0],
        [0,0,0]]


while winVal == True:
    if turn == True:
        inputVal = 1
    else:
        inputVal = 4

    print(board[0],"\n",board[1],"\n",board[2])
    command1 = int(input('how many over >')) -1
    command2 = int(input('how many down >')) -1

    if board[command2][command1] == 0:
        del board[command2][command1]
        board[command2].insert(command1,inputVal)
    else:
        print("That square is taken. Try again.")
        turn = not(turn)

    turn = not(turn)
    #Creates columns to search for wins on
    column1 = []
    for row in board:
        column1.append(row[0])

    column2 = []
    for row in board:
        column2.append(row[1])

    column3 = []
    for row in board:
        column3.append(row[2])

    a = 0    
    diagonal1 = []
    for row in board:
        diagonal1.append(row[a])
        a += 1

    a = 2
    diagonal2 = []
    for row in board:
        diagonal2.append(row[a])
        a -= 1

    for x in [3,12]:    
        winVal = sum(column1) != x and sum(column2) != x and sum(column3) != x and sum(diagonal1) != x and sum(diagonal2) != x and sum(board[0]) != x and sum(board[1]) != x and sum(board[2]) != x
        if winVal == False:
            if x == 3:
                winner = 'p1'
            elif x == 12:
                winner = 'p2'
            break
