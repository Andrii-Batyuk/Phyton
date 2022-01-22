import random
tryes = 5
secret_number = random.randint(1,20)
guess_num = 0

while secret_number != guess_num and tryes >= 1:
    guess_num = int(input("Input guess number"))
    if guess_num == secret_number:
        print("You win!")
    tryes = tryes - 1
if secret_number != guess_num and tryes == 0:
    print("You loose")