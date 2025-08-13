import random

def roll_dice(num_sides=6):
    """Simulates rolling a single dice with a specified number of sides."""
    return random.randint(1, num_sides)

def main():
    while True:
        try:
            sides = int(input("Enter the number of sides for the dice (e.g., 6 for a standard die): "))
            if sides < 1:
                print("Number of sides must be at least 1.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a number.")

    while True:
        input("Press Enter to roll the dice (or type 'q' to quit): ")
        user_input = input().lower()
        if user_input == 'q':
            break
        
        result = roll_dice(sides)
        print(f"You rolled a: {result}")

if __name__ == "__main__":
    main()