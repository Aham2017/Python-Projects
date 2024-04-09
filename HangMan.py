import random

def choose_word():
    return random.choice(["python", "hangman", "programming", "computer", "developer", 
                          "coding", "challenge", "solution", "learning", "algorithm", 
                          "language", "variable", "function", "iteration", "condition", 
                          "debugging", "software", "interface", "application", "knowledge"]).lower()

def display_word(word, guessed_letters):
    return ' '.join(letter if letter in guessed_letters else '_' for letter in word)

def draw_stickman(lives):
    return '\n'.join(["  O   ", " \|/  ", "  |   ", " / \\"][:6 - lives])

def hangman():
    word, guessed_letters, incorrect_letters, lives, won = choose_word(), set(), set(), 6, False

    print("Welcome to Hangman!")

    while lives > 0:
        print("\n" + draw_stickman(lives))
        print(f"Word: {display_word(word, guessed_letters)}")
        print(f"Incorrect letters: {', '.join(incorrect_letters) if incorrect_letters else 'None'}")

        guess = input("Guess a letter or the whole word: ").lower()

        if len(guess) == 1 and guess.isalpha():
            guessed_letters.add(guess)
            if guess not in set(word):
                incorrect_letters.add(guess)
                lives -= 1
                print(f"Incorrect guess. Lives remaining: {lives}")
        elif len(guess) == len(word) and guess.isalpha():
            won = guess == word
            lives = 0 if not won else lives
            print(f"Incorrect guess. The word was: {word}") if not won else None
        else:
            print("Invalid input. Please enter a single letter or the entire word.")
            continue

        if set(word).issubset(guessed_letters):
            won = True
            break

    print("\n" + draw_stickman(lives))
    print(f"Congratulations! You guessed the word: {word}") if won else print(f"Out of lives. The word was: {word}")

while input("Do you want to play again? (yes/no): ").lower() == "yes":
    hangman()

print("Thanks for playing! Goodbye.")