import random

total = 100


def coin_flip(guess, bet):
    chance = ["Heads", "Tails"]
    if guess == random.choice(chance):
        print("You won " + str(bet) + " euros")
        return bet
    else:
        print("You won " + str(bet) + " euros")
        return -bet


def cho_han(guess, bet):
    dice_1 = random.randint(1, 6)
    dice_2 = random.randint(1, 6)
    total = dice_1 + dice_2

    if guess == "Even" and total % 2 == 0:
        print("You won " + str(bet) + " euros!")
        return bet
    elif guess == "Odd" and total % 2 == 1:
        print("You won " + str(bet) + " euros")
        return bet
    else:
        print("You lost " + str(bet) + " euros")
        return -bet


def card_picking(bet):
    player_1 = random.randint(1, 10)
    player_2 = random.randint(1, 10)
    print("Player 1 card was " + str(player_1))
    print(("Player 2 card was " + str(player_2)))
    if player_1 > player_2:
        print("Player 1 won " + str(bet) + " euros")
        return bet
    elif player_2 > player_1:
        print("Player 2 won " + str(bet) + " euros")
        return bet
    else:
        print("It is a draw")
        return 0


def roulette(guess, bet):
    # Makes sure your bet was above 0
    if bet <= 0:
        print("------------------")
        print("Your bet should be above 0.")
        print("------------------")
        return 0

    # A standard roulette wheel has the numbers 0 through 36 as well as 00. We'll use 37 to represent 00.
    print("------------------")
    print("Let's play roulette!")
    result = random.randint(0, 37)
    if result == 37:
        print("The wheel landed on 00")
    else:
        print("The wheel landed on " + str(result))

        # Checks to see if we guessed Even and the result was even. If the result was 0, the player shouldn't win
    if guess == "Even" and result % 2 == 0 and result != 0:
        print(str(result) + " is an even number.")
        print("You won " + str(bet) + " dollars!")
        print("------------------")
        return bet

        # Checks to see if we guessed Odd and the result was odd. If the result was 37, the player shouldn't win, since that's what we are using to represent 00.
    elif guess == "Odd" and result % 2 == 1 and result != 37:
        print(str(result) + " is an odd number.")
        print("You won " + str(bet) + " dollars!")
        print("------------------")
        return bet

        # If you guessed a number and the result was that number, you should win 35 times the amount they bet
    elif guess == result:
        print("You guessed " + str(guess) + " and the result was " + str(result))
        print("You won " + str(bet * 35) + " dollars!")
        print("------------------")
        return bet * 35

        # If none of the above are true, you lost.
    else:
        print("You lost " + str(bet) + " dollars!")
        print("------------------")
        return -bet


total += coin_flip("Heads", 10)
total += card_picking(5)
total += cho_han("Even", 2)
total += roulette("Even", 10)
total += roulette(3, 1)
total += roulette("Odd", total)
print("Your total amount of money is " + str(total))