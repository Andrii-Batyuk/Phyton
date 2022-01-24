#Python home work 5
# Написать программу подсчета стоимости разговора
# для разных мобильных операторов. Пользователь вводит
# длительность разговора и выбирает с какого на какой оператор
# он звонит. Вывести стоимость на экран.

speak_time = float(input("Input how long was you call in minutes: "))
terminal_1 = input("Check first operator: MTS, Kyivstar, Life of Vodafone: ")
terminal_2 = input("Check second operator: MTS, Kyivstar, Life of Vodafone: ")
op1 = 0.8
op2 = 1.0
op3 = 0.5
op4 = 0.6
if speak_time <= 0:
    print("You type wrong time. Sorry, try again.")
elif terminal_1 == terminal_2:
    print("Your call is free :)")
elif (terminal_1 == "MTS" and terminal_2 == "Kyivstar") or (terminal_1 == "MTS" and terminal_2 == "Life") or (terminal_1 == "MTS" and terminal_2 == "Vodafone") :
    print("Your bill: ", speak_time * op1, "USD")
elif (terminal_1 == "Kyivstar" and terminal_2 == "MTS") or (terminal_1 == "Kyivstar" and terminal_2 == "Life") or (terminal_1 == "Kyivstar" and terminal_2 == "Vodafone") :
    print("Your bill: ", speak_time * op2, "USD")
elif (terminal_1 == "Life" and terminal_2 == "MTS") or (terminal_1 == "Life" and terminal_2 == "Kyivstar") or (terminal_1 == "Life" and terminal_2 == "Vodafone") :
    print("Your bill: ", speak_time * op3, "USD")
elif (terminal_1 == "Vodafone" and terminal_2 == "MTS") or (terminal_1 == "Vodafone" and terminal_2 == "Kyivstar") or (terminal_1 == "Vodafone" and terminal_2 == "Life") :
    print("Your bill: ", speak_time * op4, "USD")
else:
    print("You type wrong value. Sorry, try again.")