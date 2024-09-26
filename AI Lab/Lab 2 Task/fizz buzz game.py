import random

def fizz_buzz_logic(number):
    if number % 3 == 0 and number % 5 == 0:
        return "fizz buzz"
    elif number % 3 == 0:
        return "fizz"
    elif number % 5 == 0:
        return "buzz"
    else:
        return str(number)

def fizz_buzz_game():
    first_number = random.randint(1, 100)

    while True:
        print("First Number: ",first_number)
        player_input = input("Your answer (fizz/buzz/fizz buzz/number): ")

        correct_answer = fizz_buzz_logic(first_number)

        if player_input != correct_answer:
            print("Wrong answer. Game Over. Correct answer was:", correct_answer)
            break
        print("correct")

        second_number= random.randint(1, 100)
        print("Second Number:",second_number)

        player_input = input("Your answer (fizz/buzz/fizz buzz/number): ")

        correct_answer = fizz_buzz_logic(second_number)

        if player_input != correct_answer:
            print(f"Wrong answer. Game Over! Correct answer was {correct_answer}.")
            break
        print("correct")

        first_number += second_number
        print("Added Number:",first_number)

        player_input = input("Your answer (fizz/buzz/fizz buzz/number): ")

        correct_answer = fizz_buzz_logic(first_number)

        if player_input != correct_answer:
            print(f"Wrong answer. Game Over! Correct answer was {correct_answer}.")
            break

        random_number = random.randint(1, 100)
        print("Random Number:",random_number)
        player_input = input("Your answer (fizz/buzz/fizz buzz/number): ")

        correct_answer = fizz_buzz_logic(random_number)

        if player_input != correct_answer:
            print("Wrong answer. Game Over. Correct answer was:", correct_answer)
            break

        print("correct")

fizz_buzz_game()





