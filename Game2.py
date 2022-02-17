### Камень - ножницы - бугага:) RC_1.0   ###
#Variables
player1_score = 0
player2_score = 0
player1_choice = ''
player2_choice = ''
rounds = 3
#Start game
while True:
    for i in range(1, rounds+1):
        while player1_choice != 'r' and player1_choice != 'p' and player1_choice != 's' and player1_choice != 'l' and player1_choice != 'o':
            player1_choice = str(input("Enter your choice player 1: [r],[p],[s],[l],[o] : "))

        while player2_choice != 'r' and player2_choice != 'p' and player2_choice != 's' and player2_choice != 'l' and player2_choice != 'o':
            player2_choice = str(input("Enter your choice player 2: [r],[p],[s],[l],[o] : "))
#Compare results:
        if player1_choice == player2_choice:
            print("Draw round!")
            player1_choice = ''
            player2_choice = ''
        elif (player1_choice == 'r' and player2_choice == 's') or (player1_choice == 'r' and player2_choice == 'l') or (player1_choice == 'l' and player2_choice == 'o') or (player1_choice == 'l' and player2_choice == 'p') or (player1_choice == 'o' and player2_choice == 'r') or (player1_choice == 'o' and player2_choice == 's') or (player1_choice == 's' and player2_choice == 'p') or (player1_choice == 's' and player2_choice == 'l') or (player1_choice == 'p' and player2_choice == 'r') or (player1_choice == 'p' and player2_choice == 'o'):
            player1_score = player1_score + 1
            print("Player 1 win round!", i)
            player1_choice = ''
            player2_choice = ''
        else:
            player2_score = player2_score + 1
            print("Player 2 win round!", i)
            player1_choice = ''
            player2_choice = ''
#Print results
    if player1_score == player2_score:
        print("Draw game!")
    elif player1_score > player2_score:
        print("Player 1 win game!")
    else:
        print("Player 2 win game!")
#Play Again?
    choice = input("Play again? Press Y to continue: ")
    if choice == 'Y' or choice == 'y':
        rounds = 3
        player1_choice = ''
        player2_choice = ''
        player1_score = 0
        player2_score = 0
    else:
        break
#End of game
print("Good Bye!")
