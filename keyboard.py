from convert import str_to_float
# Purpose:
# The `gather_numbers` function prompts the user to enter numbers one by one. 
# It will collect valid numbers into a list and return that list when the user types 'done'. 
# The function uses `str_to_float` to ensure that only valid numbers are added to the list.
#
# Input:
# - The user provides input through the command line (using `input()`).
# - The user can enter any string, and if it's a valid number, it will be accepted and added to the list.
# - The user can type 'done' (case-insensitive) to stop the input process.
# 
# Output:
# - A list of valid float numbers entered by the user.
# - If no valid numbers are entered, the list will be empty.
def gather_numbers() -> list[float]:
    numbers = []
    while True:
        user_input = input("Enter a number (or type 'done' to finish): ").strip()

        if user_input.lower() == 'done':
            break

        number = str_to_float(user_input)

        if number is not None:
            numbers.append(number)
    return numbers

# Main check
if __name__ == '__main__':
    numbers = gather_numbers()
    total = sum(numbers)
    print(f"The sum of the valid numbers is: {total}")
