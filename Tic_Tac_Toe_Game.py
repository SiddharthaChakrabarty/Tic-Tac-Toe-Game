import random

def display_board(board):
    
    print(" " + " " + " " + "|" + " " + " " + " " + "|" + " " + " " + " " )
    print(" " + board[7] + " " + "|" + " " + board[8] + " " + "|" + " " + board[9] +" " )
    print("_" + "_" + "_" + "|" + "_" + "_" + "_" + "|" + "_" + "_" + "_" )
    print(" " + " " + " " + "|" + " " + " " + " " + "|" + " " + " " + " " )
    print(" " + board[4] + " " + "|" + " " + board[5] + " " + "|" + " " + board[6] +" " )
    print("_" + "_" + "_" + "|" + "_" + "_" + "_" + "|" + "_" + "_" + "_" )
    print(" " + " " + " " + "|" + " " + " " + " " + "|" + " " + " " + " " )
    print(" " + board[1] + " " + "|" + " " + board[2] + " " + "|" + " " + board[3] +" " )
    print(" " + " " + " " + "|" + " " + " " + " " + "|" + " " + " " + " " )

def player_marker():
    player1_marker = ""
    while player1_marker not in ["X","O"]:
        player1_marker = input("Player1, please choose one of X or O : ")
    if player1_marker == "X":
        player2_marker = "O"
    else:
        player2_marker = "X"
    return (player1_marker,player2_marker)

def player1_input(player1_marker):
    choice1 = 0
    
    while choice1 not in range(1,10):
        choice1 = int(input("Player1, Enter the position on the board. "))
    if board[choice1] != " ":
        print("Position not available")
        choice1 = 0
    else:
        board[choice1] = player1_marker
    

def player2_input(player2_marker):
    
    choice2 = 0
    
    while choice2 not in range(1,10):
        choice2 = int(input("Player2, Enter the position on the board. "))
    if board[choice2] != " ":
        print("Position not available")
        choice2 = 0
    else:
        board[choice2] = player2_marker

def win_or_tie(board,marker):
    full = 1    
    for x in board[1:]:
        if x == " ":
            full = 0
            break
    if (board[1] == board[2] == board[3] == marker):
        print("Congratulations!!! You have won the game.")
        return 1
    elif (board[1] == board[4] == board[7] == marker):
        print("Congratulations!!! You have won the game.")
        return 1
    elif (board[1] == board[5] == board[9] == marker):
        print("Congratulations!!! You have won the game.")
        return 1
    elif (board[2] == board[5] == board[8] == marker):
        print("Congratulations!!! You have won the game.")
        return 1
    elif (board[3] == board[6] == board[9] == marker):
        print("Congratulations!!! You have won the game.")
        return 1
    elif (board[3] == board[5] == board[7] == marker):
        print("Congratulations!!! You have won the game.")
        return 1
    elif (board[4] == board[5] == board[6] == marker):
        print("Congratulations!!! You have won the game.")
        return 1
    elif (board[7] == board[8] == board[9] == marker):
        print("Congratulations!!! You have won the game.")
        return 1
    elif full == 1:
        print("The game is tied.")
        return 1
    else:
        return 0

def game1(player1_marker):
    
    player1_input(player1_marker)
    check = win_or_tie(board,player1_marker)
    display_board(board)
    return check

def game2(player2_marker):
    
    player2_input(player2_marker)
    check = win_or_tie(board,player2_marker)
    display_board(board)
    return check

def choose_first():
    if random.randint(0,1) == 0:
        return "Player 1"
    else:
        return "Player 2"
    
def replay():
    return input("Do you want to play again? Yes or No. ").lower().startswith("y")

print("Welcome to Tic Tac Toe!!!\n")
while True:
    board = ["#"," "," "," "," "," "," "," "," "," "]
    player1_marker,player2_marker = player_marker()
    turn = choose_first()
    print(turn + " will play first \n")
    play_game = input("Are you ready to play? Enter Yes or No. \n")
    if play_game.lower()[0] == "y":
        check = 0
    else:
        check = 1
    while (check == 0 and turn == "Player 1"):
        
        check = game1(player1_marker)
        if check == 1:
            break
        check = game2(player2_marker)
        if check == 1:
            break
    while (check == 0 and turn == "Player 2"):
        
        check = game2(player2_marker)
        if check == 1:
            break
        check = game1(player1_marker)
        if check == 1:
            break
    if not replay():
        break
    
        

