# ----------------------------------------------------------
# ---------------- Number Guessing Game --------------------
# ----------------------------------------------------------

from random import randint

num_lower, num_higher = 1, 10
random_number: int = randint(num_lower,num_higher)

print (f"Guess the number in the range from {num_lower} to {num_higher}.")

# Creating infinite loop
while True:
    try:
        user_guess: int = int(input('Guess: '))
    except ValueError as e:
        print("The entered number is not valid. Please try again.")
        continue

    if user_guess > random_number:
        print('The number you wrote is lower.')
    elif user_guess < random_number:
        print('The number you wrote is higher.')
    else:
        print("This is the right number! YOU WIN!")
        break