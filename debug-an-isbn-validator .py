** start of main.py **

def validate_isbn(isbn, length):
    # Check length
    if len(isbn) != length:
        print(f'ISBN-{length} code should be {length} digits long.')
        return

    # Separate main digits and check digit
    main_digits = isbn[:-1]
    given_check_digit = isbn[-1]

    # Convert digits to integers
    try:
        main_digits_list = [int(digit) for digit in main_digits]
    except ValueError:
        print("Invalid character was found.")
        return

    # Calculate expected check digit
    if length == 10:
        expected_check_digit = calculate_check_digit_10(main_digits_list)
    else:
        expected_check_digit = calculate_check_digit_13(main_digits_list)

    # Compare check digits
    if given_check_digit == expected_check_digit:
        print("Valid ISBN Code.")
    else:
        print("Invalid ISBN Code.")


def calculate_check_digit_10(main_digits_list):
    digits_sum = 0

    for index, digit in enumerate(main_digits_list):
        digits_sum += digit * (10 - index)

    result = 11 - digits_sum % 11

    if result == 11:
        return "0"
    elif result == 10:
        return "X"
    else:
        return str(result)


def calculate_check_digit_13(main_digits_list):
    digits_sum = 0

    for index, digit in enumerate(main_digits_list):
        if index % 2 == 0:
            digits_sum += digit
        else:
            digits_sum += digit * 3

    result = 10 - digits_sum % 10

    if result == 10:
        return "0"
    else:
        return str(result)


def main():
    user_input = input("Enter ISBN and length: ")

    try:
        values = user_input.split(",")
        isbn = values[0]
        length = int(values[1])
    except IndexError:
        print("Enter comma-separated values.")
        return
    except ValueError:
        print("Length must be a number.")
        return

    if length == 10 or length == 13:
        validate_isbn(isbn, length)
    else:
        print("Length should be 10 or 13.")


# main()

** end of main.py **

