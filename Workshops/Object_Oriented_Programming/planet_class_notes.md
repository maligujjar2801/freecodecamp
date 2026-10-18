# Workshop Notes — Building a Planet Class

## Goal
Represent planets as objects, validate constructor arguments, and customize their string representation.

## Concepts
- `class Planet` defines a custom type.
- `__init__` assigns instance attributes.
- `isinstance(value, str)` checks whether an argument is a string.
- `TypeError` is raised when an argument has the wrong type.
- `ValueError` is raised when a string argument is empty.
- `orbit()` returns a message using object attributes.
- `__str__()` controls the human-readable text shown by `print(planet)`.

## Constructor validation
The constructor requires `name`, `planet_type`, and `star` to be non-empty strings. Each planet stores these values separately.

## Program flow
The program creates Earth, Jupiter, and Kepler-22b, prints each object, then prints the orbit message for each.

## Important note
The three validation checks are repeated intentionally in this beginner exercise. In a future refactor, a loop or helper method could reduce duplication without changing the behavior.

## Run
```bash
python "Build a Planet Class.py"
```
