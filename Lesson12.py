# Tic Tac Toe
# |X|_|_|
# |_|O|_|
# |_|_|X|
board_1 = '1'
board_2 = '2'
board_3 = '3'
board_4 = '4'
board_5 = '5'
board_6 = '6'
board_7 = '7'
board_8 = '8'
board_9 = '9'
turn = 'X'

player1_symol = 'X'
player2_symol = 'O'
player1_choise = 0
player2_choise = 0
count = 1

# print(board_1, board_2, board_3)
# print(board_4, board_5, board_6)
# print(board_7, board_8, board_9)


while count <= 9:
    # Game choice
    while True:
        player1_choise = str(input(f'Enter your choice {player1_symol}: '))
        # Board update
        if player1_choise == board_1:
            board_1 = player1_symol
            break
        elif player1_choise == board_2:
            board_2 = player1_symol
            break
        elif player1_choise == board_3:
            board_3 = player1_symol
            break
        elif player1_choise == board_4:
            board_4 = player1_symol
            break
        elif player1_choise == board_5:
            board_5 = player1_symol
            break
        elif player1_choise == board_6:
            board_6 = player1_symol
            break
        elif player1_choise == board_7:
            board_7 = player1_symol
            break
        elif player1_choise == board_8:
            board_8 = player1_symol
            break
        elif player1_choise == board_9:
            board_9 = player1_symol
            break
    board = f'{board_1}|{board_2}|{board_3}\n-----\n{board_4}|{board_5}|{board_6}\n-----\n{board_7}|{board_8}|{board_9}'
    print(board)


    while True:
        player2_choise = str(input(f'Enter your choice {player2_symol}: '))
        # Board update
        if player2_choise == board_1:
            board_1 = player2_symol
            break
        elif player2_choise == board_2:
            board_2 = player2_symol
            break
        elif player2_choise == board_3:
            board_3 = player2_symol
            break
        elif player2_choise == board_4:
            board_4 = player2_symol
            break
        elif player2_choise == board_5:
            board_5 = player2_symol
            break
        elif player2_choise == board_6:
            board_6 = player2_symol
            break
        elif player2_choise == board_7:
            board_7 = player2_symol
            break
        elif player2_choise == board_8:
            board_8 = player2_symol
            break
        elif player2_choise == board_9:
            board_9 = player2_symol
            break
    board = f'{board_1}|{board_2}|{board_3}\n-----\n{board_4}|{board_5}|{board_6}\n-----\n{board_7}|{board_8}|{board_9}'
    print(board)

    count = count + 1