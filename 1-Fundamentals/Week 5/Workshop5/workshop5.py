import random as r


def guess_random_number(tries, start, stop):
    num = r.randint(start, stop)
    guesses = []

    while tries != 0:
        print(f'Number of tries left: {tries}')
        tries -= 1

        while True:
            try:
                guess = int(
                    input(f'Guess a number between {start} and {stop}: '))

                if guess in guesses:
                    print("You can't pick the same integer twice.")
                    continue
                else:
                    guesses.append(guess)

                break
            except ValueError:
                print("Please enter integers only.  Try again...")

        if guess == num:
            print("You guessed the correct number!")
            break
        elif guess < num:
            print("Guess higher!")
        else:
            print("Guess lower!")

        if tries == 0:
            print("You have failed to guess the number:", num)


def guess_random_num_linear(tries, start, stop):
    num = r.randint(start, stop)
    print(f'The number for the program to guess is: {num}')

    while tries != 0:

        for i in range(start, stop+1):
            print(f'Number of tries left: {tries}')
            tries -= 1
            guess = i
            print(f'The program is guessing... {guess}')

            if guess == num:
                print("The program has guessed the correct number!")
                return True
            elif guess < num:
                print("Guess higher!")
            else:
                print("Guess lower!")

            if tries == 0:
                print("The program has failed to guess the correct number.")
                return False


def guess_random_num_binary(tries, start, stop):
    num = r.randint(start, stop)
    print(f'The number for the program to guess is: {num}')

    while tries != 0:

        print(f'Number of tries left: {tries}')
        tries -= 1

        guess = ((stop - start) // 2) + start

        print(f'The program is guessing... {guess}')

        if guess == num:
            print("The program has guessed the correct number!")
            return
        elif guess < num:
            print("Guessing higher!")
            start = guess + 1
        else:
            print("Guessing lower!")
            stop = guess - 1

        if tries == 0:
            print("The program has failed to guess the correct number.")
            break


def user_game_parameters():
    tries = int(input("How many tries would you like? \n"))
    start = int(
        input("From which integer would you like the numbers to start? \n"))
    stop = int(input("At which integer would you like the numbers to stop? \n"))
    return (tries, start, stop)


def user_guess_method():
    (tries, start, stop) = user_game_parameters()
    choice = input(
        "Enter 1 for user guess, 2 for linear guess, or 3 for binary guess: \n")

    if choice == '1':
        guess_random_number(tries, start, stop)
    elif choice == '2':
        guess_random_num_linear(tries, start, stop)
    elif choice == '3':
        guess_random_num_binary(tries, start, stop)
    else:
        print('Make better choices!')
        return


def gambling(bet_max=10, bet_size=1):

    while bet_max != 0 and bet_max < 50:
        print(
            f'You have a total of ${bet_max} to gamble.  The minimum bet is ${bet_size}.')
        bet = int(input("Place your bet! "))

        if guess_random_num_linear(1, 0, 1):
            print(f'\nCongrats!  You win ${bet}!')
            bet_max += bet
        else:
            print(f'\nSorry, you lost ${bet}!')
            bet_max -= bet

    if bet_max == 0:
        print("You're broke!  Go home.")
    else:
        print(f'You have ${bet_max}!  Take the money and run!')


# guess_random_number(5,0,10)
# guess_random_num_linear(5,0,10)
# guess_random_num_binary(5, 0, 100)

# user_guess_method()
gambling()
