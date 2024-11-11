from convert import str_to_float
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
