import random

print("H A N G M A N\n")

win = 0
loss = 0

def game():
    word_list = ["python", "java", "swift", "javascript"]
    chosen_word = random.choice(word_list)
    hidden_word = ["-" for i in range(len(chosen_word))]
    
    global win
    global loss
    past_guess = list()
    attempt = 0

    while attempt < 8:
        print("".join(hidden_word))
        guess = input("Input a letter: ")

        if len(guess) != 1:
            print("Please, input a single letter.\n")
        elif guess.isalpha() is False or guess.islower() is False:
            print("Please, enter a lowercase letter from the English alphabet.\n")
        elif guess in past_guess:
            print("You've already guessed this letter.\n")
        elif guess not in chosen_word:
            print("That letter doesn't appear in the word.\n")
            attempt += 1
            past_guess.extend(guess)
        elif guess not in hidden_word:
            for i in range(len(chosen_word)):
                if chosen_word[i] == guess:
                    hidden_word[i] = guess
                    past_guess.extend(guess)
                    print()

        if chosen_word == "".join(hidden_word):
            print(f"You guessed the word {chosen_word}!")
            print("You survived!")
            win += 1
            ask()

    else:
        print("You lost!")
        loss += 1
        ask()

def ask():
    menu = input('Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ')
    if menu == "play":
        game()
    elif menu == "results":
        print(f"You won: {win} times.")
        print(f"You lost: {loss} times.")
        ask()
    elif menu == "exit":
        exit()
    else:
        ask()

ask()
