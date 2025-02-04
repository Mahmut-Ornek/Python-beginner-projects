import random
import string
from words import words




def get_valid_word(words):

    word = random.choice(words) # chooses a random word from the list 
    while "-" in word or " " in word:
        word = random.choice(words)

    return word.upper()




def hangman():

    word = get_valid_word(words) # calling the function to get a word
    word_letters = set(word) 
    alphabet = set(string.ascii_uppercase)

    used_letters = set() # empty set for used letters

    lives = 6 
    while len(word_letters)>0 and lives>0:

        print("You have ", lives, "lives left and you have used this letters: ", " ".join(used_letters))

        # create a list of letters of word
        # if the letter is in used letter then show the letter 
        # if not use "-" instead of letter. For example, "A - - A -" , A is a used letter

        word_list = [letter if letter in used_letters else "-" for letter in word]


        print("Current word: ", " ".join(word_list))

        user_letter = input("\nGuess a letter: ").upper() # this takes an upper letter as an input from user

        #check if input is in used letter or not
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter) 
            if user_letter in word_letters: 
                word_letters.remove(user_letter) 
            else:
                lives-=1
                print("Letter is not in the word.")
        
        elif user_letter in used_letters:
            print("You have alredy used this letter. Please try again.")
        else:
            print("Invalid char. Please try again.")

    #when the loop ends, either you guessed the word or you have no lives remained
    if lives == 0:
        print("Sorry, you died. The word was", word,".")
    else:
        print("You guessed the word", word, ".")


print(hangman())