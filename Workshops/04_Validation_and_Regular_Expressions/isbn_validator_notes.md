# Workshop Notes — Debugging an ISBN Validator

## Goal
Check ISBN-10 and ISBN-13 check digits and practice validating user input.

## Functions
- `validate_isbn(isbn, length)` checks the supplied length, separates the main digits from the check digit, calculates the expected digit, and compares the two.
- `calculate_check_digit_10(main_digits_list)` applies descending weights from 10 to 1 and handles the special check value `X`.
- `calculate_check_digit_13(main_digits_list)` alternates weights of 1 and 3.
- `main()` parses comma-separated user input and accepts only lengths 10 or 13.

## Concepts
- Slicing: `isbn[:-1]` selects all characters except the last; `isbn[-1]` selects the last character.
- `enumerate` supplies an index and a digit.
- `try/except` handles conversion errors.
- The ISBN check digit is used to detect many common transcription errors.

## Important notes
- The file contains freeCodeCamp wrapper lines named `** start of main.py **` and `** end of main.py **`. These are platform markers, not Python syntax. Remove those marker lines in a separate runnable copy if you want to execute it as a standalone script; the repository copy is preserved as submitted.
- The call to `main()` is commented out, so even after removing the markers, the interactive flow will not start until that call is enabled.
- The validator converts the main digits but does not fully validate the format of the final check-digit character before comparison.

## Run
Use the freeCodeCamp exercise environment, or create a standalone copy without the wrapper markers and enable `main()`.
