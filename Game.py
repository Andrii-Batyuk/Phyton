#Guess my number


import random

magic_number = random.randint(1, 20)
attempts = 5
guess_number = 0
counter = 0
score_player = 0
score_comp = 0


while guess_number != magic_number and attempts > 0:
    print(f"Attempt № {counter+1} and {attempts-1} attempts left.")
    guess_number = int(input("Input guess number (1-20): "))
    while guess_number <= 0 or guess_number > 20:
        guess_number = int(input("Input CORRECT (1-20) number : "))
    attempts -= 1
    counter += 1
    if guess_number == magic_number and attempts > 0:
        print(f"You win with attempt № {counter}. And MAGIC NUMBER IS *** {guess_number} *** !!!")
        score_player += 1
        print(f"Score: Player: {score_player}. Computer: {score_comp}")
        check = str(input("Input Yes if you want to play more : "))
        if check == "y" or check == "Yes" or check == "YEs" or check == "YES" or check == "yes":
            attempts = 5
            magic_number = random.randint(1, 20)
            counter = 0
    if guess_number != magic_number and attempts == 0:
        print("You loose!")
        score_comp += 1
        print(f"Score: Player: {score_player}. Computer: {score_comp}")
        check = str(input("Input Yes if you want to play more : "))
        if check == "y" or check == "Yes" or check == "YEs" or check == "YES" or check == "yes":
            attempts = 5
            magic_number = random.randint(1, 20)
            counter = 0

print("See You!")