# Python Workshops

This directory groups Python practice files by the main concept they demonstrate. Each topic folder contains the original exercise file(s) and matching Markdown notes. Source files have been moved without intentionally changing their code.

## Topics

| Folder | Topics |
|---|---|
| [01 Python Basics](01_Python_Basics/) | `input()`, variables, type conversion, and data types |
| [02 Collections](02_Collections/) | Sets, subset/superset, union, intersection, and symmetric difference |
| [03 Object-Oriented Programming](03_Object_Oriented_Programming/) | Classes, objects, attributes, methods, validation, and `__str__` |
| [04 Validation and Regular Expressions](04_Validation_and_Regular_Expressions/) | Data validation, `re.fullmatch`, and ISBN check digits |
| [05 Functions and Configuration](05_Functions_and_Configuration/) | Functions, loops, string building, and dictionary configuration |
| [06 Data Structures](06_Data_Structures/) | Linked lists, nodes, and references |
| [07 Recursion](07_Recursion/) | Recursive calls, base cases, and building a count-up list |

## Notes and source preservation

- Notes are stored beside the Python exercise they explain.
- The original recursion notes are retained in [07 Recursion/Notes.md](07_Recursion/Notes.md).
- Some freeCodeCamp files contain platform wrapper markers such as `** start of main.py **`; these markers are not valid Python syntax outside the exercise interface. The original exercise content is preserved.
- This is a learning repository, so the notes call out known issues in the submitted examples rather than silently rewriting the original solutions.

## Running a script

Open a topic folder and run a regular standalone script with Python, for example:

```bash
python "Report card printer.py"
```

Some exercises require the freeCodeCamp environment or a separate cleaned copy before they can run as ordinary Python files.
