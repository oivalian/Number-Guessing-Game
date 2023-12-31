import random
import time
import os


# print a prompt
# print("Hello World!")
# A fun idea would be to create a number guessing game based off 'x'.
# 'x' should be randomly generated each time
# The user would be asked to guess a number
# If guessed number is higher than x, prompt 'x' is greater than 'guess'
# Vice versa as to lower (less then 'guess')


def on_launch():
    os.system('cls')
    time.sleep(4)
    print("The Number Guessing Game (v1.01)\nby oivalian")
    time.sleep(2)
    os.system('cls')
    time.sleep(2)
    main_menu()


def main_menu():
    print("\n| =-=-=-=-=-=-=-=   THE NUMBER GUESSING GAME    =-=-=-=-=-=-=-= |")
    print("Created by oivalian\n\n\n")
    time.sleep(1)
    print("|----- MAIN MENU -----|\n")
    print("[1] STANDARD MODE\n[2] HARD MODE\n[3] CHANGELOG\n[4] EXIT\n")
    menu_selection()


def menu_selection():
    time.sleep(0.5)
    match input("Select an option: "):
        case "1":
            time.sleep(2)
            os.system('cls')
            time.sleep(1)
            print("\nInitializing...")
            time.sleep(2)
            os.system('cls')
            sm_intro()
        case "2":
            time.sleep(2)
            os.system('cls')
            hm_menu()
        case "3":
            time.sleep(2)
            os.system('cls')
            changelog()
        case "4":
            time.sleep(2)
            os.system('cls')
            on_exit()
        case _:
            print("\nInvalid input!\n")
            time.sleep(2)
            os.system('cls')
            main_menu()


def on_exit():
    time.sleep(2)
    print("\n   GOODBYE FRIEND ... ")
    time.sleep(3)
    os.system('cls')
    time.sleep(1)
    exit()

#  understand cases for the above

def changelog():
    print("\n| =-=-=-=-=-=-=-=   THE NUMBER GUESSING GAME    =-=-=-=-=-=-=-= |")
    time.sleep(2)

    with open("changelog.txt", "r") as file:
        change = [entries.strip() for entries in file]
        for lines in change:
            print(lines)
    menu_return()


def menu_return():
    match input("\nInput 'M' To return to main menu: "):
        case "M" | "m":
            time.sleep(1)
            os.system('cls')
            main_menu()
        case _:
            print("\nInvalid input!\n")
            menu_return()


# eventually make limited restart attempts for standard (maybe 2 times max per level)


def sm_intro():
    print("\n|----- STANDARD MODE INTRODUCTION -----|\n\n")
    time.sleep(1)
    print("The rules of game are as follows:\n")
    print("1) Each level will generate a random number")
    print("2) You have to guess the number generated by the game")
    print("3) You have limited amount of guesses per level")
    print("4) Guess incorrectly, you lose (1) attempt and will have to restart the level")
    print("5) Guess correctly, you proceed to the next level")
    print("6) There are (5) levels total")
    print("7) Complete the game and you will get the secret code for 'Hard Mode'")
    time.sleep(2)
    match input("\nAre you ready? Y | N\n\n> "):
        case "Y" | "y":
            time.sleep(2)
            os.system('cls')
            level1()
        case "N" | "n":
            time.sleep(2)
            os.system('cls')
            main_menu()
        case _:
            time.sleep(1)
            print("\nYou must enter Y or N!\n")
            time.sleep(1)
            os.system('cls')
            sm_intro()


def level1():
    time.sleep(1)
    print("\nGOOD LUCK")
    time.sleep(2)
    os.system('cls')
    time.sleep(2)

    random_number1 = int(random.randint(1, 10))
    attempt = int(5)
    print("\n| =-=-=-=-=-=-=-=   THE NUMBER GUESSING GAME    =-=-=-=-=-=-=-= |")
    time.sleep(1)
    print("\n|----- LEVEL 1 -----|\n")
    while attempt > 0:
        time.sleep(1)
        print("I am thinking of a number between 1 and 10. You have " + str(attempt) + " attempts remaining.\n")
        try:
            answer = int(input("Type a number to play:\n\n> "))
            if answer > random_number1:
                time.sleep(1)
                attempt = attempt - int(1)
                print(f"\nThe number is lower than {answer}.\n")
                time.sleep(1)
            elif answer < random_number1:
                time.sleep(1)
                attempt = attempt - int(1)
                print(f"\nThe number is higher than {answer}.\n")
                time.sleep(1)
            elif answer == random_number1:
                time.sleep(1)
                print(f"\nYou guessed the number correctly! The number is {answer}.")
                time.sleep(3)
                os.system('cls')
                end_level1()
        except ValueError:
            print("\nYou must enter a number!\n")
        if attempt == 0:
            os.system('cls')
            time.sleep(2)
            print("\n|----- GAME OVER! -----|\n")
            time.sleep(1)
            print("The number was " + str(random_number1) + "!\n")
            time.sleep(1)
            match input("Would you like to restart the level? Y | N\n\n"):
                case "Y" | "y":
                    time.sleep(1)
                    os.system('cls')
                    time.sleep(1)
                    level1()
                case "N" | "n":
                    time.sleep(1)
                    os.system('cls')
                    main_menu()
                case _:
                    time.sleep(1)
                    print("\nYou must enter Y or N!")
                    time.sleep(2)
                    print("\nRestarting anyway...")
                    time.sleep(1)
                    os.system('cls')
                    time.sleep(1)
                    level1()


def end_level1():
    time.sleep(1)
    match input("\nPROCEED TO LEVEL 2? Y | N\n\n"):
        case "Y"| "y":
            time.sleep(2)
            os.system('cls')
            time.sleep(2)
            level2()
        case "N" | "n":
            time.sleep(1)
            os.system('cls')
            main_menu()
        case _:
            time.sleep(1)
            print("\nYou must enter Y or N!\n")
            time.sleep(1)
            os.system('cls')
            end_level1()


def level2():
    time.sleep(1)
    print("\nGOOD LUCK")
    time.sleep(2)
    os.system('cls')
    time.sleep(2)

    random_number2 = int(random.randint(1, 50))
    attempt = int(6)
    print("\n| =-=-=-=-=-=-=-=   THE NUMBER GUESSING GAME    =-=-=-=-=-=-=-= |")
    time.sleep(1)
    print("\n|----- LEVEL 2 -----|\n")
    while attempt > 0:
        time.sleep(1)
        print("I am thinking of a number between 1 and 50. You have " + str(attempt) + " attempts remaining.\n")
        try:
            answer = int(input("Type a number to play:\n\n> "))
            if answer > random_number2:
                time.sleep(1)
                attempt = attempt - int(1)
                print(f"\nThe number is lower than {answer}.\n")
                time.sleep(1)
            elif answer < random_number2:
                time.sleep(1)
                attempt = attempt - int(1)
                print(f"\nThe number is higher than {answer}.\n")
                time.sleep(1)
            elif answer == random_number2:
                time.sleep(1)
                print(f"\nYou guessed the number correctly! The number is {answer}.")
                time.sleep(3)
                os.system('cls')
                end_level2()
        except ValueError:
            print("\nYou must enter a number!\n")
        if attempt == 0:
            os.system('cls')
            time.sleep(2)
            print("\n|----- GAME OVER! -----|\n")
            time.sleep(1)
            print("The number was " + str(random_number2) + "!\n")
            time.sleep(1)
            match input("Would you like to restart the level? Y | N\n\n"):
                case "Y" | "y":
                    time.sleep(1)
                    os.system('cls')
                    time.sleep(1)
                    level2()
                case "N" | "n":
                    time.sleep(3)
                    os.system('cls')
                    main_menu()
                case _:
                    time.sleep(1)
                    print("\nYou must enter Y or N!")
                    time.sleep(2)
                    print("\nRestarting anyway...")
                    time.sleep(1)
                    os.system('cls')
                    time.sleep(1)
                    level2()


def end_level2():
    time.sleep(1)
    match input("\nPROCEED TO LEVEL 3? Y | N\n\n"):
        case "Y"| "y":
            time.sleep(2)
            os.system('cls')
            time.sleep(2)
            level3()
        case "N" | "n":
            time.sleep(1)
            os.system('cls')
            main_menu()
        case _:
            time.sleep(1)
            print("\nYou must enter Y or N!\n")
            time.sleep(1)
            os.system('cls')
            end_level2()


def level3():
    time.sleep(1)
    print("\nGOOD LUCK")
    time.sleep(2)
    os.system('cls')
    time.sleep(2)

    random_number3 = int(random.randint(1, 100))
    attempt = int(7)
    print("\n| =-=-=-=-=-=-=-=   THE NUMBER GUESSING GAME    =-=-=-=-=-=-=-= |")
    time.sleep(1)
    print("\n|----- LEVEL 3 -----|\n")
    time.sleep(1)
    while attempt > 0:
        time.sleep(1)
        print("I am thinking of a number between 1 and 100. You have " + str(attempt) + " attempts remaining.\n")
        try:
            answer = int(input("Type an number to play:\n\n> "))
            if answer > random_number3:
                time.sleep(1)
                attempt = attempt - int(1)
                print(f"\nThe number is lower than {answer}\n")
                time.sleep(1)
            elif answer < random_number3:
                time.sleep(1)
                attempt = attempt - int(1)
                print(f"\nThe number is higher than {answer}\n")
                time.sleep(1)
            elif answer == random_number3:
                time.sleep(1)
                print(f"\nYou guessed the number correctly! The number is {answer}.")
                time.sleep(3)
                os.system('cls')
                end_level3()
        except ValueError:
            print("\nYou must enter a number!\n")
        if attempt == 0:
            os.system('cls')
            time.sleep(2)
            print("\n|----- GAME OVER -----|\n")
            time.sleep(1)
            print("The number was " + str(random_number3) + "!\n")
            time.sleep(1)
            match input("Would you like to restart the level? Y | N\n\n"):
                case "Y" | "y":
                    time.sleep(1)
                    os.system('cls')
                    time.sleep(1)
                    level3()
                case "N" | "n":
                    time.sleep(3)
                    os.system('cls')
                    main_menu()
                case _:
                    print("\nYou must enter Y or N!")
                    time.sleep(2)
                    print("\nRestarting anyway...")
                    time.sleep(1)
                    os.system('cls')
                    time.sleep(1)
                    level3()


def end_level3():
    time.sleep(1)
    match input("\nPROCEED TO LEVEL 4? Y | N\n\n"):
        case "Y"| "y":
            time.sleep(2)
            os.system('cls')
            time.sleep(2)
            level4()
        case "N" | "n":
            time.sleep(1)
            os.system('cls')
            main_menu()
        case _:
            time.sleep(1)
            print("\nYou must enter Y or N!\n")
            time.sleep(1)
            os.system('cls')
            end_level3()


def level4():
    time.sleep(1)
    print("\nGOOD LUCK")
    time.sleep(2)
    os.system('cls')
    time.sleep(2)

    random_number4 = int(random.randint(1, 500))
    attempt = int(9)
    print("\n| =-=-=-=-=-=-=-=   THE NUMBER GUESSING GAME    =-=-=-=-=-=-=-= |")
    time.sleep(1)
    print("\n|----- LEVEL 4 -----|\n")
    time.sleep(1)
    while attempt > 0:
        time.sleep(1)
        print("I am thinking of a number between 1 and 500. You have " + str(attempt) + " attempts remaining.\n")
        try:
            answer = int(input("Type a number to play:\n\n> "))
            if answer > random_number4:
                time.sleep(1)
                attempt = attempt - int(1)
                print(f"\nThe number is lower than {answer}\n")
                time.sleep(1)
            elif answer < random_number4:
                time.sleep(1)
                attempt = attempt - int(1)
                print(f"\nThe number is higher than {answer}\n")
                time.sleep(1)
            elif answer == random_number4:
                time.sleep(1)
                print(f"\nYou guessed the number correctly! The number is {answer}.")
                time.sleep(3)
                os.system('cls')
                end_level4()
        except ValueError:
            print("\nYou must enter a number!\n")
        if attempt == 0:
            os.system('cls')
            time.sleep(2)
            print("\n|----- GAME OVER -----|\n")
            time.sleep(1)
            print("The number was " + str(random_number4) + "!\n")
            time.sleep(1)
            restart = input("Would you like to restart the level? Y | N\n\n")
            if restart.upper() == "Y":
                time.sleep(1)
                os.system('cls')
                time.sleep(1)
                level4()
            elif restart.upper() == "N":
                time.sleep(1)
                print("\nThanks for playing!\n")
                time.sleep(3)
                os.system('cls')
                main_menu()
            else:
                time.sleep(1)
                print("\nYou must enter Y or N!")
                time.sleep(2)
                print("\nRestarting anyway...")
                time.sleep(1)
                os.system('cls')
                time.sleep(1)
                level4()


def end_level4():
    time.sleep(1)
    next_level = input("\nProceed to 'Final Level'? Y | N\n\n")
    if next_level.upper() == "Y":
        time.sleep(2)
        os.system('cls')
        time.sleep(2)
        final_level()
    elif next_level.upper() == "N":
        time.sleep(1)
        print("\nThanks for playing!")
        time.sleep(3)
        os.system('cls')
        time.sleep(2)
        main_menu()
    else:
        time.sleep(1)
        print("\nYou must enter Y or N!\n")
        time.sleep(1)
        os.system('cls')
        end_level4()


def final_level():
    time.sleep(1)
    print("\nGOOD LUCK")
    time.sleep(2)
    os.system('cls')
    time.sleep(2)

    random_number5 = int(random.randint(1, 1000))
    attempt = int(10)
    print("\n| =-=-=-=-=-=-=-=   THE NUMBER GUESSING GAME    =-=-=-=-=-=-=-= |")
    time.sleep(1)
    print("\n|----- FINAL LEVEL -----|\n")
    time.sleep(1)
    while attempt > 0:
        time.sleep(1)
        print("I am thinking of a number between 1 and 1000. You have " + str(attempt) + " attempts remaining.\n")
        try:
            answer = int(input("Type a number to play:\n\n> "))
            if answer > random_number5:
                time.sleep(1)
                attempt = attempt - int(1)
                print(f"\nThe number is lower than {answer}\n")
                time.sleep(1)
            elif answer < random_number5:
                time.sleep(1)
                attempt = attempt - int(1)
                print(f"\nThe number is higher than {answer}\n")
                time.sleep(1)
            elif answer == random_number5:
                time.sleep(1)
                print(f"\nYou guessed the number correctly! The number is {answer}.")
                time.sleep(3)
                os.system('cls')
                end_final_level()
        except ValueError:
            print("\nYou must enter a number!\n")
        if attempt == 0:
            os.system('cls')
            time.sleep(2)
            print("\n|----- GAME OVER -----|\n")
            time.sleep(1)
            print("The number was " + str(random_number5) + "!\n")
            time.sleep(1)
            restart = input("Would you like to restart the level? Y | N\n\n")
            if restart.upper() == "Y":
                time.sleep(1)
                os.system('cls')
                time.sleep(1)
                final_level()
            elif restart.upper() == "N":
                time.sleep(1)
                print("\nThanks for playing!\n")
                time.sleep(3)
                os.system('cls')
                main_menu()
            else:
                time.sleep(1)
                print("\nYou must enter Y or N!")
                time.sleep(2)
                print("\nRestarting anyway...")
                time.sleep(1)
                os.system('cls')
                time.sleep(1)
                final_level()


def end_final_level():
    time.sleep(1)
    print("\n| =-=-=-=-=-=-=-=-=   CONGRATULATIONS!    =-=-=-=-=-=-=-=-= |\n")
    time.sleep(2)
    print("YOU FINISHED THE GAME!\n")
    time.sleep(2)
    print("NOW TRY YOUR LUCK ON 'HARD MODE' ;-)")
    time.sleep(3)
    os.system('cls')
    time.sleep(2)
    print("\nThe secret code for 'Hard Mode' is 'RANDOMISE'")
    time.sleep(3)
    print("\n\n\nGood luck ;-)")
    time.sleep(2)
    os.system('cls')
    time.sleep(1)
    main_menu()


# make the below work as a try statement


def hm_menu():
    time.sleep(1)
    print("\n| =-=-=-=-=-=-=-=   THE NUMBER GUESSING GAME    =-=-=-=-=-=-=-= |\n\n")
    time.sleep(1)
    print("I see you are interested in Hard Mode. Do you have the secret code?")
    print("(Hint: Beat Standard Mode!)\n")
    time.sleep(1)
    print("What do you want to do?\n")
    print("[1] Enter secret word")
    print("[2] Return to Main Menu\n")
    hm_selection = input("Select an option: ")
    if hm_selection == "1":
        time.sleep(1)
        os.system('cls')
        hm_lock()
    elif hm_selection == "2":
        time.sleep(1)
        os.system('cls')
        main_menu()
    else:
        print("\nYou must enter a number!\n")
        time.sleep(1)
        os.system('cls')
        time.sleep(1)
        hm_menu()


def hm_lock():
    time.sleep(2)
    secret_word = input("\nEnter the secret word: ")
    if secret_word.upper() == "RANDOMISE":
        time.sleep(2)
        os.system('cls')
        time.sleep(1)
        print("\nInitializing...")
        time.sleep(2)
        os.system('cls')
        time.sleep(1)
        hm_intro()
    else:
        time.sleep(2)
        print(f"\nTHE SECRET WORD IS NOT {secret_word}\n")
        time.sleep(2)
        os.system('cls')
        time.sleep(2)
        hm_menu()


def hm_intro():
    time.sleep(1)
    print("\n|----- HARD MODE MODE INTRODUCTION -----|\n\n")
    time.sleep(1)
    print("The rules of 'Hard Mode' are as follows:\n")
    time.sleep(1)
    print("1) Each level will generate a random number")
    time.sleep(1)
    print("2) You have to guess the number generated by the game")
    time.sleep(1)
    print("3) You have limited amount of attempts per level")
    time.sleep(1)
    print("3) You have one less attempt per level compared to 'Standard Mode'")
    time.sleep(1)
    print("4) Guess incorrectly, you lose (1) attempt and will have to restart from level 1")
    time.sleep(1)
    print("5) Guess correctly, you proceed to the next level")
    time.sleep(1)
    print("6) There are (5) levels total")
    time.sleep(2)
    start = input("\nAre you ready? Y | N\n\n")
    if start.upper() == "Y":
        time.sleep(2)
        os.system('cls')
        time.sleep(1)
        print("\nGOOD LUCK")
        time.sleep(2)
        os.system('cls')
        time.sleep(2)
        hm_level1()
    if start.upper() == "N":
        time.sleep(2)
        os.system('cls')
        main_menu()
    else:
        time.sleep(1)
        print("\nYou must enter Y or N!\n")
        time.sleep(2)
        os.system('cls')
        time.sleep(1)
        hm_intro()


def hm_level1():
    random_number1 = int(random.randint(1, 10))
    attempt = int(4)
    print("\n| =-=-=-=-=-=-=-=   THE NUMBER GUESSING GAME    =-=-=-=-=-=-=-= |")
    time.sleep(1)
    print("\n|----- HARD MODE - LEVEL 1 -----|\n")
    time.sleep(1)
    while attempt > 0:
        time.sleep(1)
        print("I am thinking of a number between 1 and 10. You have " + str(attempt) + " attempts remaining.\n")
        try:
            answer = int(input("Type a number to play:\n\n> "))
            if answer > random_number1:
                time.sleep(1)
                attempt = attempt - int(1)
                print(f"\nThe number is lower than {answer}.\n")
                time.sleep(1)
            elif answer < random_number1:
                time.sleep(1)
                attempt = attempt - int(1)
                print(f"\nThe number is higher than {answer}.\n")
                time.sleep(1)
            elif answer == random_number1:
                time.sleep(1)
                print(f"\nYou guessed the number correctly! The number is {answer}.")
                time.sleep(3)
                os.system('cls')
                end_hm_level1()
        except ValueError:
            print("\nYou must enter a number!\n")
        if attempt == 0:
            os.system('cls')
            time.sleep(2)
            print("\n|----- GAME OVER! -----|\n")
            time.sleep(1)
            print("The number was " + str(random_number1) + "!\n")
            time.sleep(1)
            restart = input("Would you like to restart? Y | N\n\n")
            if restart.upper() == "Y":
                time.sleep(1)
                os.system('cls')
                time.sleep(1)
                hm_level1()
            elif restart.upper() == "N":
                time.sleep(1)
                print("\nThanks for playing!\n")
                time.sleep(3)
                os.system('cls')
                main_menu()
            else:
                time.sleep(1)
                print("\nYou must enter Y or N!")
                time.sleep(2)
                print("\nRestarting ;-)")
                time.sleep(1)
                os.system('cls')
                time.sleep(1)
                hm_level1()


def end_hm_level1():
    time.sleep(1)
    play_again = input("\nPROCEED TO 'LEVEL 2'? Y | N\n\n")
    if play_again.upper() == "Y":
        time.sleep(2)
        os.system('cls')
        time.sleep(2)
        hm_level2()
    elif play_again.upper() == "N":
        time.sleep(1)
        print("\nThanks for playing!")
        time.sleep(3)
        os.system('cls')
        main_menu()
    else:
        time.sleep(1)
        print("\nYou must enter Y or N!\n")
        time.sleep(1)
        os.system('cls')
        end_hm_level1()


def hm_level2():
    random_number2 = int(random.randint(1, 50))
    attempt = int(5)
    print("\n| =-=-=-=-=-=-=-=   THE NUMBER GUESSING GAME    =-=-=-=-=-=-=-= |")
    time.sleep(1)
    print("\n|----- HARD MODE - LEVEL 2 -----|\n")
    time.sleep(1)
    while attempt > 0:
        time.sleep(1)
        print("I am thinking of a number between 1 and 50. You have " + str(attempt) + " attempts remaining.\n")
        try:
            answer = int(input("Type a number to play:\n\n"))
            if answer > random_number2:
                time.sleep(1)
                attempt = attempt - int(1)
                print(f"\nThe number is lower than {answer}\n")
                time.sleep(1)
            elif answer < random_number2:
                time.sleep(1)
                attempt = attempt - int(1)
                print(f"\nThe number is higher than {answer}\n")
                time.sleep(1)
            elif answer == random_number2:
                time.sleep(1)
                print(f"\nYou guessed the number correctly! The number is {answer}.")
                time.sleep(3)
                os.system('cls')
                end_hm_level2()
        except ValueError:
            print("\nYou must enter a number!\n")
        if attempt == 0:
            os.system('cls')
            time.sleep(2)
            print("\n|----- GAME OVER -----|\n")
            time.sleep(1)
            print("The number was " + str(random_number2) + "!\n")
            time.sleep(1)
            restart = input("Would you like to restart? Y | N\n\n")
            if restart.upper() == "Y":
                time.sleep(1)
                os.system('cls')
                time.sleep(1)
                hm_level1()
            elif restart.upper() == "N":
                time.sleep(1)
                print("\nThanks for playing!\n")
                time.sleep(3)
                os.system('cls')
                main_menu()
            else:
                print("\nYou must enter Y or N!")
                time.sleep(2)
                print("\nRestarting anyway ;-)")
                time.sleep(1)
                os.system('cls')
                time.sleep(1)
                hm_level1()


def end_hm_level2():
    time.sleep(1)
    play_again = input("\nPROCEED TO 'LEVEL 3'? Y | N\n\n")
    if play_again.upper() == "Y":
        time.sleep(2)
        os.system('cls')
        time.sleep(2)
        hm_level3()
    elif play_again.upper() == "N":
        time.sleep(1)
        print("\nThanks for playing!")
        time.sleep(3)
        os.system('cls')
        main_menu()
    else:
        time.sleep(1)
        print("\nYou must enter Y or N!\n")
        time.sleep(1)
        os.system('cls')
        end_hm_level2()


def hm_level3():
    random_number3 = int(random.randint(1, 100))
    attempt = int(6)
    print("\n| =-=-=-=-=-=-=-=   THE NUMBER GUESSING GAME    =-=-=-=-=-=-=-= |")
    time.sleep(1)
    print("\n|----- HARD MODE - LEVEL 3 -----|\n")
    time.sleep(1)
    while attempt > 0:
        time.sleep(1)
        print("I am thinking of a number between 1 and 100. You have " + str(attempt) + " attempts remaining.\n")
        try:
            answer = int(input("Type a number to play:\n\n> "))
            if answer > random_number3:
                time.sleep(1)
                attempt = attempt - int(1)
                print(f"\nThe number is lower than {answer}.\n")
                time.sleep(1)
            elif answer < random_number3:
                time.sleep(1)
                attempt = attempt - int(1)
                print(f"\nThe number is higher than {answer}.\n")
                time.sleep(1)
            elif answer == random_number3:
                time.sleep(1)
                print(f"\nYou guessed the number correctly! The number is {answer}.")
                time.sleep(3)
                os.system('cls')
                end_hm_level3()
        except ValueError:
            print("\nYou must enter a number!\n")
        if attempt == 0:
            os.system('cls')
            time.sleep(2)
            print("\n|----- GAME OVER! -----|\n")
            time.sleep(1)
            print("The number was " + str(random_number3) + "!\n")
            time.sleep(1)
            restart = input("Would you like to restart? Y | N\n\n")
            if restart.upper() == "Y":
                time.sleep(1)
                os.system('cls')
                time.sleep(1)
                hm_level1()
            elif restart.upper() == "N":
                time.sleep(1)
                print("\nThanks for playing!\n")
                time.sleep(3)
                os.system('cls')
                main_menu()
            else:
                time.sleep(1)
                print("\nYou must enter Y or N!")
                time.sleep(2)
                print("\nRestarting anyway ;-)")
                time.sleep(1)
                os.system('cls')
                time.sleep(1)
                hm_level1()


def end_hm_level3():
    time.sleep(1)
    play_again = input("\nPROCEED TO 'LEVEL 4'? Y | N\n\n")
    if play_again.upper() == "Y":
        time.sleep(2)
        os.system('cls')
        time.sleep(2)
        hm_level4()
    elif play_again.upper() == "N":
        time.sleep(1)
        print("\nThanks for playing!")
        time.sleep(3)
        os.system('cls')
        main_menu()
    else:
        time.sleep(1)
        print("\nYou must enter Y or N!\n")
        time.sleep(1)
        os.system('cls')
        end_hm_level1()


def hm_level4():
    random_number4 = int(random.randint(1, 500))
    attempt = int(8)
    print("\n| =-=-=-=-=-=-=-=   THE NUMBER GUESSING GAME    =-=-=-=-=-=-=-= |")
    time.sleep(1)
    print("\n|----- HARD MODE - LEVEL 4 -----|\n")
    time.sleep(1)
    while attempt > 0:
        time.sleep(1)
        print("I am thinking of a number between 1 and 500. You have " + str(attempt) + " attempts remaining.\n")
        try:
            answer = int(input("Type a number to play:\n\n> "))
            if answer > random_number4:
                time.sleep(1)
                attempt = attempt - int(1)
                print(f"\nThe number is lower than {answer}.\n")
                time.sleep(1)
            elif answer < random_number4:
                time.sleep(1)
                attempt = attempt - int(1)
                print(f"\nThe number is higher than {answer}.\n")
                time.sleep(1)
            elif answer == random_number4:
                time.sleep(1)
                print(f"\nYou guessed the number correctly! The number is {answer}.")
                time.sleep(3)
                os.system('cls')
                end_hm_level4()
        except ValueError:
            print("\nYou must enter a number!\n")
        if attempt == 0:
            os.system('cls')
            time.sleep(2)
            print("\n|----- GAME OVER! -----|\n")
            time.sleep(1)
            print("The number was " + str(random_number4) + "!\n")
            time.sleep(1)
            restart = input("Would you like to restart? Y | N\n\n")
            if restart.upper() == "Y":
                time.sleep(1)
                os.system('cls')
                time.sleep(1)
                hm_level1()
            elif restart.upper() == "N":
                time.sleep(1)
                print("\nThanks for playing!\n")
                time.sleep(3)
                os.system('cls')
                main_menu()
            else:
                time.sleep(1)
                print("\nYou must enter Y or N!")
                time.sleep(2)
                print("\nRestarting anyway ;-)")
                time.sleep(1)
                os.system('cls')
                time.sleep(1)
                hm_level1()


def end_hm_level4():
    time.sleep(1)
    play_again = input("\nPROCEED TO 'FINAL LEVEL'? Y | N\n\n")
    if play_again.upper() == "Y":
        time.sleep(2)
        os.system('cls')
        time.sleep(2)
        hm_final_level()
    elif play_again.upper() == "N":
        time.sleep(1)
        print("\nThanks for playing!")
        time.sleep(3)
        os.system('cls')
        main_menu()
    else:
        time.sleep(1)
        print("\nYou must enter Y or N!\n")
        time.sleep(1)
        os.system('cls')
        end_hm_level1()


def hm_final_level():
    random_number5 = int(random.randint(1, 1000))
    attempt = int(9)
    print("\n| =-=-=-=-=-=-=-=   THE NUMBER GUESSING GAME    =-=-=-=-=-=-=-= |")
    time.sleep(1)
    print("\n|----- HARD MODE - FINAL LEVEL -----|\n")
    time.sleep(1)
    while attempt > 0:
        time.sleep(1)
        print("I am thinking of a number between 1 and 1000. You have " + str(attempt) + " attempts remaining.\n")
        try:
            answer = int(input("Type a number to play:\n\n> "))
            if answer > random_number5:
                time.sleep(1)
                attempt = attempt - int(1)
                print(f"\nThe number is lower than {answer}.\n")
                time.sleep(1)
            elif answer < random_number5:
                time.sleep(1)
                attempt = attempt - int(1)
                print(f"\nThe number is higher than {answer}.\n")
                time.sleep(1)
            elif answer == random_number5:
                time.sleep(1)
                print(f"\nYou guessed the number correctly! The number is {answer}.")
                time.sleep(3)
                os.system('cls')
                end_hm_final_level()
        except ValueError:
            print("\nYou must enter a number!\n")
        if attempt == 0:
            os.system('cls')
            time.sleep(2)
            print("\n|----- GAME OVER! -----|\n")
            time.sleep(1)
            print("The number was " + str(random_number5) + "!\n")
            time.sleep(1)
            restart = input("Would you like to restart? Y | N\n\n")
            if restart.upper() == "Y":
                time.sleep(1)
                os.system('cls')
                time.sleep(1)
                hm_level1()
            elif restart.upper() == "N":
                time.sleep(1)
                print("\nThanks for playing!\n")
                time.sleep(3)
                os.system('cls')
                main_menu()
            else:
                time.sleep(1)
                print("\nYou must enter Y or N!")
                time.sleep(2)
                print("\nRestarting anyway ;-)")
                time.sleep(1)
                os.system('cls')
                time.sleep(1)
                hm_level1()


def end_hm_final_level():
    time.sleep(1)
    print("\n| =-=-=-=-=-=-=-=-=   CONGRATULATIONS!    =-=-=-=-=-=-=-=-= |\n")
    time.sleep(2)
    print("YOU FINISHED THE GAME ON HARD MODE!\n")
    time.sleep(2)
    print("YOU CLEARLY HAVE TOO MUCH TIME ON YOUR HANDS...\n\n\n\n")
    time.sleep(3)
    print("MAYBE THERE IS A SECRET MODE?")
    time.sleep(2)
    os.system('cls')
    time.sleep(1)
    main_menu()


on_launch()
