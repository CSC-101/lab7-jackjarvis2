import sys
from convert import str_to_float
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


