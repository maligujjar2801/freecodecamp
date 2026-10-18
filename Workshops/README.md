# Python Workshops

This directory groups Python practice files by the main concept they demonstrate. Each topic folder contains the original exercise file(s) and matching Markdown notes. Source files have been moved without intentionally changing their code.

## Topics

| Folder | Topics |
|---|---|
| [Python Basics](Python_Basics/) | `input()`, variables, type conversion, and data types |
| [Collections](Collections/) | Sets, subset/superset, union, intersection, and symmetric difference |
| [Object-Oriented Programming](Object_Oriented_Programming/) | Classes, objects, attributes, methods, validation, and `__str__` |
| [Validation and Regular Expressions](Validation_and_Regular_Expressions/) | Data validation, `re.fullmatch`, and ISBN check digits |
| [Functions and Configuration](Functions_and_Configuration/) | Functions, loops, string building, and dictionary configuration |
| [Data Structures](Data_Structures/) | Linked lists, nodes, and references |
| [Recursion](Recursion/) | Recursive calls, base cases, and building lists recursively |

## Recursion lab

- [Count Up — source file](Recursion/countup%20function.py)
- [Count Up — notes](Recursion/Notes.md)
- [Range of Numbers Generator — source file](Recursion/range_of_numbers.py)
- [Range of Numbers Generator — detailed notes](Recursion/range_of_numbers_notes.md)

## Notes and source preservation

- Notes are stored beside the Python exercise they explain.
- Existing recursion notes and exercise files are retained.
- Some freeCodeCamp files contain platform wrapper markers such as `** start of main.py **`; these markers are not valid Python syntax outside the exercise interface. The original exercise content is preserved.
- This is a learning repository, so the notes call out known issues in the submitted examples rather than silently rewriting the original solutions.

## Running a script

Open a topic folder and run a regular standalone script with Python, for example:

```bash
python "Report card printer.py"
```

Some exercises require the freeCodeCamp environment or a separate cleaned copy before they can run as ordinary Python files.
