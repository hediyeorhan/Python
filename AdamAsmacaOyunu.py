import random

print("\nWelcome to the game Hangman!\nI am thinking of a word that is 5 letters long.\n-------------------------------------------------")
words = ["apple", "alone", "among", "angle", "area"]
secret_word = random.choice(words)
guesses = len(secret_word) + 5
available_letters = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","r","p","q","r","s","t","u","v","w","y","z"]
line = len(secret_word) * "_"
list_line = []
for i in line:
    list_line += i
print(list_line)
print("Available Letters = {}".format(available_letters))


def is_word_guessed(secret_word,letters_guessed):
    Control = False
    for index, value in enumerate(secret_word):
        if secret_word[index] == letters_guessed:
            list_line[index] = value
            Control = True

    return Control

def get_guessed_word(secret_word,letters_guessed):

    if is_word_guessed(secret_word,letters_guessed) == True:
        for index, value in enumerate(secret_word):
            if secret_word[index] == letters_guessed:
                list_line[index] = value
    else:
        pass
    return list_line

def get_available_letters(letters_guessed):
    global available_letters
    for k in available_letters:
        if k == letters_guessed:
            del_index = available_letters.index(k)
            del available_letters[del_index]

    return available_letters

while guesses != 0:

    letters_guessed = input("Please guess a letter : ")
    guesses -= 1
    function1 = is_word_guessed(secret_word, letters_guessed)

    if function1 == True:
        function2 = get_guessed_word(secret_word, letters_guessed)
        print("\n-------------------------------------------------\n")
    else:
        function2 = get_guessed_word(secret_word, letters_guessed)
        print("\nThis letter is not found in the word.\n-------------------------------------------------\n")

    if (guesses == 0):
        print("You have no right to guess.\n\nWORD : {}\n".format(secret_word))
        break

    if not "_" in function2:
        print(list_line)
        print("\nCongratulations, you won\nWORD : {}".format(secret_word))
        break


    print("You have {} guesses left.".format(guesses))
    print(function2)
    print("Available Letters = {}".format(get_available_letters(letters_guessed)))








