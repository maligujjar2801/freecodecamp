# Workshop Notes — Input, Variables, and Data Types

## Goal
Practice receiving user input, converting text to numeric values, storing a Boolean, and checking types.

## Concepts
- `input(prompt)` displays a prompt and returns the user's response as a **string**.
- `int(value)` converts a suitable string to an integer.
- `float(value)` converts a suitable string to a floating-point number.
- `type(value)` reports an object's type.
- `isinstance(value, float)` checks whether a value is an instance of `float`.
- `True` is a Boolean value.

## Program flow
1. Read a name and print it with its type.
2. Store and inspect a Boolean value in `is_student`.
3. Convert the age input to an integer.
4. Convert the score input to a float and check its type.

## Example
If the user enters `Ali`, `17`, and `86.4`, the age becomes `17` (an `int`) and the score becomes `86.4` (a `float`).

## Important notes
- Input is text until converted.
- Invalid numeric input causes `ValueError`; later projects can handle this with `try/except`.
- The comments showing example values are only comments; they do not set the variables.
- The script is an introductory input/type demonstration, despite its filename.

## Run
```bash
python "Report card printer.py"
```
