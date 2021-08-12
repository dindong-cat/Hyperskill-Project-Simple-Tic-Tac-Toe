board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
game_continue = 1
X_OR_O = None

def board_display():
    print("---------")
    print(f"| {board[0][0]} {board[0][1]} {board[0][2]} |")
    print(f"| {board[1][0]} {board[1][1]} {board[1][2]} |")
    print(f"| {board[2][0]} {board[2][1]} {board[2][2]} |")
    print("---------")


def coordinate():
    global X_OR_O
    while game_continue:
        step = input("Enter the coordinates: ")
        if step.replace(" ", "").isnumeric():
            if (int(step[0]) >= 1 and int(step[-1]) >= 1) and (int(step[0]) <= 3 and int(step[-1]) <= 3):
                step = step.split()
                if len(step) == 2:
                    step = "".join(step)  # str(11)
                    if board[int(step[0])-1][int(step[-1])-1] == " ":
                        if X_OR_O == None or [i for j in board for i in j].count("X") == [i for j in board for i in j].count("O"):
                            X_OR_O = "X"
                        else:
                            X_OR_O = "O"
                        board[int(step[0])-1][int(step[-1])-1] = X_OR_O
                        status_judgement()
                        break
                    else:
                        print("This cell is occupied! Choose another one!")
            else:
                print("Coordinates should be from 1 to 3!")
        else:
            print("You should enter numbers!")


def status_judgement():
    global game_continue
    board_display()
    current = [i for j in board for i in j]
    if current.count(" ") >= 1 and current.count(" ") <= 8:
        if board[0][0] == board[1][1] == board[2][2] == "X":
            print("X wins")
            game_continue = 0
        elif board[0][0] == board[1][1] == board[2][2] == "O":
            print("O wins")
            game_continue = 0
        elif board[0][2] == board[1][1] == board[2][0] == "X":
            print("X wins")
            game_continue = 0
        elif board[0][2] == board[1][1] == board[2][0] == "O":
            print("O wins")
            game_continue = 0
        else:
            for i in range(0, 3):
                if board[i][0] == board[i][1] == board[i][2] == "X":
                    print("X wins")
                    game_continue = 0
                    break
                elif board[i][0] == board[i][1] == board[i][2] == "O":
                    print("O wins")
                    game_continue = 0
                    break
                elif board[0][i] == board[1][i] == board[2][i] == "X":
                    print("X wins")
                    game_continue = 0
                    break
                elif board[0][i] == board[1][i] == board[2][i] == "O":
                    print("O wins")
                    game_continue = 0
                    break
                else:
                    coordinate()
    elif current.count(" ") == 0:
        if board[0][0] == board[1][1] == board[2][2] == "X":
            print("X wins")
            game_continue = 0
        elif board[0][0] == board[1][1] == board[2][2] == "O":
            print("O wins")
            game_continue = 0
        elif board[0][2] == board[1][1] == board[2][0] == "X":
            print("X wins")
            game_continue = 0
        elif board[0][2] == board[1][1] == board[2][0] == "O":
            print("O wins")
            game_continue = 0
        else:
            print("Draw")
            game_continue = 0


board_display()
coordinate()

"""winner = [board[0][0:3],
  board[1][0:3],
  board[2][0:3],
  [board[0][0], board[1][0], board[2][0]],
  [board[0][1], board[1][1], board[2][1]],
  [board[0][2], board[1][2], board[2][2]],
  [board[0][0], board[1][1], board[2][2]],
  [board[0][2], board[1][1], board[2][0]]]"""


"""current = [i for j in board for i in j]
if current.count(" ") >= 1:
    for i in winner:
        print(i)
        if i[0] == i[1] == i[2] == "X":
            print("X wins")
            game_continue = 0
            break
        elif all(i) == "O":
            print("O wins")
            game_continue = 0
            break
        else:
            coordinate()
            break
else:
    for i in winner:
        if i[0] == i[1] == i[2] == "X":
            print("X wins")
            game_continue = 0
            break
        elif i[0] == i[1] == i[2] == "O":
            print("O wins")
            game_continue = 0
            break
        else:
            print("Draw")
            game_continue = 0
            break"""
