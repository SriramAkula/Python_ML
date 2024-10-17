import random

def choose_difficulty():
    print("\nSelect a Difficulty Level:")
    print("1. Easy (Numbers between 1-10, 5 attempts)")
    print("2. Medium (Numbers between 1-50, 7 attempts)")
    print("3. Hard (Numbers between 1-100, 10 attempts)")
    
    while True:
        choice = input("Enter your choice (1, 2, or 3): ")
        if choice == '1':
            return 1, 10, 5
        elif choice == '2':
            return 2, 50, 7
        elif choice == '3':
            return 3, 100, 10
        else:
            print("Invalid choice! Please choose 1, 2, or 3.")

def calculate_score(attempts_used, total_attempts, difficulty_level):
    base_score = difficulty_level * 100
    bonus_for_remaining_attempts = (total_attempts - attempts_used) * 10
    total_score = base_score + bonus_for_remaining_attempts
    return max(total_score, 0)

def play_guessing_game():
    print("\nWelcome to the Number Guessing Game!")
    difficulty_level, upper_bound, max_attempts = choose_difficulty()
    target_number = random.randint(1, upper_bound)
    attempts_used = 0

    print(f"\nI have selected a number between 1 and {upper_bound}.")
    print(f"You have {max_attempts} attempts to guess the correct number!")

    while attempts_used < max_attempts:
        try:
            guess = int(input(f"\nAttempt {attempts_used + 1}: What's your guess? "))

            if guess < 1 or guess > upper_bound:
                print(f"Please enter a number between 1 and {upper_bound}.")
                continue

            attempts_used += 1

            if guess < target_number:
                print("Too low! Try a higher number.")
            elif guess > target_number:
                print("Too high! Try a lower number.")
            else:
                print(f"\nYou got it! The correct number was {target_number}.")
                print(f"You took {attempts_used} attempts.")
                score = calculate_score(attempts_used, max_attempts, difficulty_level)
                print(f"Your score is: {score}")
                break
        except ValueError:
            print("Invalid input! Please enter a valid number.")
    
    if attempts_used == max_attempts:
        print(f"\nYou've used all {max_attempts} attempts. The correct number was {target_number}.")

def ask_to_play_again():
    while True:
        choice = input("\nWould you like to play again? (y/n): ").lower()
        if choice == 'y':
            return True
        elif choice == 'n':
            print("Thanks for playing! Goodbye!")
            return False
        else:
            print("Invalid input! Please enter 'y' to play again or 'n' to quit.")

def start_game():
    while True:
        play_guessing_game()
        if not ask_to_play_again():
            break

start_game()
