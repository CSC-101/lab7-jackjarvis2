import sys
from convert import str_to_float
# Purpose: 
# The `process_arguments` function takes a list of string arguments, converts them into floating-point numbers if valid, 
# and sums up the valid numbers. It returns the total sum of valid numbers.

# Input:
# - A list of string arguments (each string may represent a number).
# - For example: ['1.5', '3', 'abc', '2.5'] (where 'abc' is not a valid number and should be ignored).

# Output:
# - A floating-point number representing the sum of all valid numbers.
# - For example, for input ['1.5', '3', 'abc', '2.5'], the output would be 1.5 + 3 + 2.5 = 7.0.
def process_arguments(args) -> float:
    total = 0.0
    for arg in args:
        number = str_to_float(arg)
        if number is not None:
            total += number
    return total


# Main check
if __name__ == '__main__':
    arguments = sys.argv[1:]

    total_sum = process_arguments(arguments)

    print(f"The sum of the valid numbers is: {total_sum}")


