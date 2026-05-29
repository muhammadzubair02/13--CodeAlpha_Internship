import random

country =['pakistan', 'china', 'india', 'russia', 'iran']
attempts = 6
word = random.choice(country)
word_len = len(word)
display_dash = ["_"] * word_len
print("word: "," ".join(display_dash))
user_guess = ""
guessed_letters = []

while "_" in display_dash and attempts > 0:
    user_guess = input("Guess a letter: ")

    #Check repeated guess
    if user_guess in guessed_letters:
        print("You already guessed this letter!")
        attempts -= 1
        print("Attempts left:", attempts)
        continue
    guessed_letters.append(user_guess)

    #Check the user guess
    if user_guess in word:
        for i in range(word_len):
            if word[i] == user_guess:
                display_dash[i] = user_guess
    else:
        attempts -= 1 
        print("Wrong! Attempts left:", attempts)
    print(" ".join(display_dash))


#Display the result
if "_" not in display_dash:
    print("You guessed the word:", word)
else:
    print("Game Over! The word was:", word)