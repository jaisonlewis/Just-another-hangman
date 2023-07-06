import random
import string

def ran_wrd_picker(): #picks random words from a text file in the
    with open("hangman.txt", "r") as file:
        data = file.read()
        words = data.split()
        word_pos = random.randint(0, len(words) - 1)
        return words[word_pos].upper()

def hangman(): #logic for the game
    word = ran_wrd_picker()
    '''print(word) #cheat code here ;D'''
    word_letters = set(word)
    alphabet = set(string.ascii_uppercase)
    used_letters = set()

    while len(word_letters) > 0: #loop for guessing the correct word
        print("You have used these letters: ", ' '.join(used_letters))
        word_list = [letter if letter in used_letters else "—" for letter in word]
        print("Current word: ", " ".join(word_list))
        user_input = input("Guess a letter: ").upper()

        if user_input in alphabet - used_letters:
            used_letters.add(user_input)
            if user_input in word_letters:
                word_letters.remove(user_input)
            else:
                print("Incorrect guess!")

        elif user_input in used_letters:
            print("You have already used this letter, type another")
        else:
            print("Type in a valid letter")

    print("Congratulations the secret word is ", (word))