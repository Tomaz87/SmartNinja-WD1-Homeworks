secret = 7
guess = int(input("Guess the secret number (between 1 and 50): "))

if secret == guess:
    print("Congrats! You've guessed the secret number! It is number: 7")
else:
    print("Sorry, you've missed it. Try again!")