'''
file: LuckyNumber.py
name: Jonathan Robinson
date: 10-2-25
course: CIS 25-26
Steps: # Main game loop - play multiple rounds
# TODO: Use while True loop with break statement here

    # Generate random lucky number
    # TODO: Use random.randint() to generate number between 1 and 50
   
    # Set maximum attempts
    # TODO: Set max_attempts to 7
   
    # Initialize attempt counter
    # TODO: Create attempts variable starting at 0
   
    print(f"\nRound {total_rounds + 1}")
    print("I'm thinking of a lucky number between 1 and 50...")
    print(f"You have {max_attempts} attempts to guess it!")
    print()
   
    # Guessing loop - count-controlled while loop
    # TODO: Use while loop that continues while attempts < max_attempts
   
        # Get user's guess
        # TODO: Get input and convert to integer
       
        # Increment attempt counter
        # TODO: Add 1 to attempts
       
        # Check if guess is correct
        # TODO: Compare guess to lucky_number
       
            # Player wins!
            # TODO: Display success message
            # TODO: Update statistics
            # TODO: Break out of guessing loop
           
        # Provide hints
        # TODO: Tell user if guess is too high or too low
       
    # If loop completes without break, player lost
    # TODO: Handle case where player runs out of attempts
   
    # Display round statistics
    # TODO: Show attempts used, win/loss for this round
   
    # Ask if player wants to play again
    # TODO: Get input and check if user wants to continue
    # TODO: Use break statement to exit main game loop if done

# Display final statistics
# TODO: Show total rounds, wins, and average guesses per round

print("\nThanks for playing! Goodbye!")
'''
import random

# Game statistics
total_rounds = 0
total_wins = 0
total_guesses = 0

print("=" * 50)
print("  WELCOME TO THE LUCKY NUMBER GUESSING GAME!")
print("=" * 50)
print()


# Main game loop - play multiple rounds
while True:
    lucky_number = random.randint(1, 35)  # Generate random lucky number
    max_attempts = 7                      # Set maximum attempts
    attempts = 0                          # Initialize attempt counter

    print(f"\nRound {total_rounds + 1}")
    print("I'm thinking of a lucky number between 1 and 35...")
    print(f"You have {max_attempts} attempts to guess it!")
    print()

    win = False
    while attempts < max_attempts:         # Guessing loop
        try:
            guess = int(input(f"Attempt {attempts + 1}: Enter your guess: "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        attempts += 1
        total_guesses += 1

        if guess == lucky_number:
            print(f"Congratulations! You guessed the lucky number {lucky_number} in {attempts} attempts!")
            total_wins += 1
            win = True
            break
        elif guess < lucky_number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

    if not win:
        print(f"Sorry, you've used all {max_attempts} attempts. The lucky number was {lucky_number}.")

    total_rounds += 1
    print(f"Round {total_rounds} stats: Attempts used: {attempts}, {'Win' if win else 'Loss'}")

    play_again = input("Do you want to play another round? (y/n): ").strip().lower()
    if play_again != 'y':
        break

# Display final statistics
if total_rounds > 0:
    avg_guesses = total_guesses / total_rounds
else:
    avg_guesses = 0
print("\nGame Over!")
print(f"Total rounds played: {total_rounds}")
print(f"Total wins: {total_wins}")
print(f"Average guesses per round: {avg_guesses:.2f}")