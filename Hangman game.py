import random

# List of predefined words
words = ['apple', 'grape', 'mango', 'peach', 'lemon']

# Select a random word from the list
word_to_guess = random.choice(words)
guessed_letters = []
incorrect_guesses = 0
max_guesses = 6

# Create a display version of the word with underscores
display_word = ['_' for _ in word_to_guess]

print("Welcome to Hangman!")
print("Guess the word letter by letter.")
print("You have", max_guesses, "incorrect guesses allowed.\n")

while incorrect_guesses < max_guesses and '_' in display_word:
    print("Word:", ' '.join(display_word))
    print("Guessed letters:", ' '.join(guessed_letters))
    guess = input("Enter a letter: ").lower()

    # Input validation
    if not guess.isalpha() or len(guess) != 1:
        print("Please enter a single alphabet letter.\n")
        continue

    if guess in guessed_letters:
        print("You already guessed that letter.\n")
        continue

    guessed_letters.append(guess)

    if guess in word_to_guess:
        print("Correct!\n")
        for i in range(len(word_to_guess)):
            if word_to_guess[i] == guess:
                display_word[i] = guess
    else:
        incorrect_guesses += 1
        print(f"Wrong! You have {max_guesses - incorrect_guesses} guesses left.\n")

# Game result
if '_' not in display_word:
    print("Congratulations! You guessed the word:", word_to_guess)
else:
    print("Game Over! The word was:", word_to_guess)
