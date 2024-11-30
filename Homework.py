import datetime

# Get all the month names
months = [datetime.date(2024, month, 1).strftime('%B') for month in range(1, 13)]

#Display each month
print("The months of the year are:  ")
for month in months:
    print(month)

print("-------------------------------------------------------")
# Function to generate squares of numbers in a given range
def generate_squares(start, end):
    squares = [i ** 2 for i in range(start, end + 1)]
    return squares

# Function to separate odd and even squares
def separate_odd_even(squares):
    odd_squares = [square for square in squares if square % 2 != 0]
    even_squares = [square for square in squares if square % 2 == 0]
    return odd_squares, even_squares

# Main program
start_range = int(input("Enter the start of the range: "))  # e.g., 2
end_range = int(input("Enter the end of the range: "))  # e.g., 10

# Generate squares
squares = generate_squares(start_range, end_range)

# Separate into odd and even squares
odd_squares, even_squares = separate_odd_even(squares)

# Display results
print(f"\nSquares of numbers from {start_range} to {end_range}:\n{squares}")
print(f"\nOdd squares:\n{odd_squares}")
print(f"\nEven squares:\n{even_squares}")
