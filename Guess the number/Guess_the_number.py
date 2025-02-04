import random


def guess(x):

    random_number= random.randint(1,x)
    guess=0
    i =0
    print("\nDO NOT FORGET THAT YOU HAVE ONLY 5 CHANCE TO GUESS!!!\n\n")

    while guess!=random_number:

        if i<=4:
            guess = int(input(f"Guess the number between 1 and {x}: "))

            if guess < random_number:
                print("The number is too low, guess again!")
            elif guess > random_number:
                print("The number is too high, guess again!")
            elif guess == random_number:
                print(f"Excellent! Your final guess is correct! The number was {random_number}.")
                break

            i += 1
            print(f"You've  remained {5-i} chances!")
            print("\n--------------------------------------\n")
        else:
            print(f"Sorry, no chances remained. The actual number was {random_number}.")
            break

    print("See you next time...")




def computer_guess(x):
    low = 1
    high = x
    feedback =""

    while feedback!= "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low #or high, doesn't matter
        
        feedback = input(f"Is {guess} too high (H), too low (L), or correct (C)???").lower()

        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1
    
    print(f"The computer guessed your number {guess}, correctly...")

computer_guess(1000)