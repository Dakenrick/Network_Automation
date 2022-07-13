#Learn Python - Full Course for Beginners freeCodeCamp.org Youtube
#Lesson Building a Guessing Game: using if statements, while loops, dictionaries, etc.

secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of Guesses, YOU LOSE")
else:
    print("You win!")