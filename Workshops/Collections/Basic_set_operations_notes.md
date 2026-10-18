# Workshop Notes — Python Set Operations

## Goal
Explore set creation, adding and discarding values, set relationships, and common set operations.

## Concepts
- `set()` creates an empty set.
- `.add(value)` inserts a value; duplicates are stored only once.
- `.discard(value)` removes a value if present without raising an error if it is absent.
- `.issubset(other)` checks whether every item in a set appears in another set.
- `.issuperset(other)` checks whether a set contains every item from another set.
- `.isdisjoint(other)` is true when two sets have no shared items.
- `|` is union, `&` is intersection, and `^` is symmetric difference.

## Set operations
- **Union:** all distinct values from either set.
- **Intersection:** only values shared by both sets.
- **Symmetric difference:** values in either set but not both.

## Important notes
- Sets are unordered, so printed element order is not guaranteed.
- Set elements must be hashable.
- The variable name `interscshn` and the spelling in the output messages are retained from the original exercise; clearer names such as `intersection` are preferable in new code.

## Run
```bash
python "Basic set operations..py"
```
