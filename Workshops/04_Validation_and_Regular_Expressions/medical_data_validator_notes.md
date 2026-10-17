# Workshop Notes — Medical Data Validation with `re`

## Goal
Validate a collection of medical-record dictionaries using type checks, allowed values, and regular expressions.

## Concepts
- `import re` loads Python's regular-expression module.
- `re.fullmatch(pattern, value, re.IGNORECASE)` checks that the entire string matches a pattern without case sensitivity.
- `isinstance` checks value types.
- `all(...)` verifies that every item in a collection meets a condition.
- `enumerate(data)` provides each record's index and value.
- `set(dictionary.keys())` makes it possible to compare a record's keys against the required key set.
- `**dictionary` passes dictionary entries as keyword arguments.

## Validation rules represented
- Patient IDs should begin with P/p and continue with digits.
- Ages must be integers at least 18.
- Gender is restricted to male or female, ignoring capitalization.
- Diagnosis may be a string or `None`.
- Medications must be a list of strings.
- Visit IDs should begin with V/v and continue with digits.

## Important review finding
The current `validate()` function calculates `invalid_records` but does not use that list to set `is_invalid` or report the invalid fields. As a result, some field-level validation failures can still lead to a final “Valid format.” message. This note documents the existing script; it does not silently change the original exercise.

## Privacy note
The included records are sample data. Do not put real patient-identifying or medical information in a public learning repository.

## Run
```bash
python "Build a medical data validator by using re modue..py"
```
