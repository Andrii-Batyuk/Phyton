import requests
import random
private_key = '5225844010:AAFlzde2mJddWhDDkoT1v-FNg6sAQa4IrMg'
url = f'https://api.telegram.org/bot{private_key}/'
player2_choice = ''
def game():
    ### Камень - ножницы - бугага:) RC_1.0   ###
    # Variables
    player1_score = 0
    player2_score = 0
    player1_choice = ''
    player2_choice = ''
    rounds = 3
    # Start game
    while True:
        for i in range(1, rounds + 1):
            while player1_choice != 'r' and player1_choice != 'p' and player1_choice != 's' and player1_choice != 'l' and player1_choice != 'o':
                player1_choice = str(input("Enter your choice player 1: [r],[p],[s],[l],[o] : "))

            while player2_choice != 'r' and player2_choice != 'p' and player2_choice != 's' and player2_choice != 'l' and player2_choice != 'o':
                player2_choice = str(input("Enter your choice player 2: [r],[p],[s],[l],[o] : "))
            # Compare results:
            if player1_choice == player2_choice:
                print("Draw round!")
                player1_choice = ''
                player2_choice = ''
            elif (player1_choice == 'r' and player2_choice == 's') or (
                    player1_choice == 'r' and player2_choice == 'l') or (
                    player1_choice == 'l' and player2_choice == 'o') or (
                    player1_choice == 'l' and player2_choice == 'p') or (
                    player1_choice == 'o' and player2_choice == 'r') or (
                    player1_choice == 'o' and player2_choice == 's') or (
                    player1_choice == 's' and player2_choice == 'p') or (
                    player1_choice == 's' and player2_choice == 'l') or (
                    player1_choice == 'p' and player2_choice == 'r') or (
                    player1_choice == 'p' and player2_choice == 'o'):
                player1_score = player1_score + 1
                print("Player 1 win round!", i)
                player1_choice = ''
                player2_choice = ''
            else:
                player2_score = player2_score + 1
                print("Player 2 win round!", i)
                player1_choice = ''
                player2_choice = ''
        # Print results
        if player1_score == player2_score:
            print("Draw game!")
        elif player1_score > player2_score:
            print("Player 1 win game!")
        else:
            print("Player 2 win game!")
        # Play Again?
        choice = input("Play again? Press Y to continue: ")
        if choice == 'Y' or choice == 'y':
            rounds = 3
            player1_choice = ''
            player2_choice = ''
            player1_score = 0
            player2_score = 0
        else:
            break
    # End of game
    print("Good Bye!")

def last_update(request):
    response = requests.get(request + 'getUpdates')
    response = response.json()
    results = response['result']
    total_updates = len(results) - 1
    return results[total_updates]


def get_chat_id(update):
    chat_id = update['message']['chat']['id']
    return chat_id


def get_message_text(update):
    message_text = update['message']['text']
    return message_text


def send_message(chat, text):
    params = {'chat_id': chat, 'text': text}
    response = requests.post(url + 'sendMessage', data=params)
    return response


def main():
    update_id = last_update(url)['update_id']
    while True:
        update = last_update(url)
        if update_id == update['update_id']:
            if get_message_text(update).lower() == 'hi' or get_message_text(
                    update).lower() == 'hello' or get_message_text(update).lower() == 'hey':

                send_message(get_chat_id(update), "Greetings! Type 'Dice or Rock'")
            elif get_message_text(update).lower() == 'dice':
                _1 = random.randint(1, 6)
                _2 = random.randint(1, 6)
                send_message(get_chat_id(update),
                             'You have ' + str(_1) + ' and ' + str(_2) + '!\nYour result is ' + str(_1 + _2) + '!')
            elif get_message_text(update).lower() == 'rock':
                send_message(get_chat_id(update),
                                "Enter your choice player 1: [r],[p],[s],[l],[o] : ")
                player1_choice = get_message_text(update).lower()
                send_message(get_chat_id(update),
                             player1_choice)
            else:
                send_message(get_chat_id(update), "Sorry, I don't undersand you :" )
            update_id += 1


if __name__ == '__main__':
    main()
