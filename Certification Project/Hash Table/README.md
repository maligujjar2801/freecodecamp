# Build a Hash Table — freeCodeCamp

A Python implementation of a hash table using a character-sum hash function and nested dictionaries for collision handling.

## Files

- `hash_table.py` — implementation of `HashTable` with `hash`, `add`, `remove`, and `lookup` methods.
- `detailed_notes.md` — concepts, line-by-line logic, examples, edge cases, tests, and complexity.

## Run

Requires Python 3.

```bash
python hash_table.py
```

The script demonstrates hashing, lookup, collision handling, and safe removal.

## Example

```python
from hash_table import HashTable

table = HashTable()
table.add("golf", "sport")

print(table.hash("golf"))  # 424
print(table.lookup("golf"))  # sport
```

## Collision handling

The hash function sums the Unicode code points of each character. Different keys can produce the same sum, so the outer dictionary maps each hash to an inner dictionary containing the original key-value pairs.

For example, `"dear"` and `"read"` both hash to `412`, but both entries remain stored in the same bucket.

## Methods

| Method | Purpose |
|---|---|
| `hash(key)` | Sum the Unicode code points in the key |
| `add(key, value)` | Add or update a key-value pair |
| `remove(key)` | Remove a key safely if it exists |
| `lookup(key)` | Return the value or `None` |

See [detailed_notes.md](detailed_notes.md) for the full explanation and test cases.
