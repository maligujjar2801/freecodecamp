# Build a Hash Table — Detailed Notes

## 1. Project overview

This project implements a basic hash table from scratch, following the freeCodeCamp lab requirements.

A **hash table** stores key-value pairs. A hash function transforms a key into a number used to select a storage bucket. Because different keys can produce the same hash, the implementation must handle **collisions**.

### Learning objectives

- Define a Python class and initialize instance state.
- Convert characters to numeric code points with `ord()`.
- Build a hash function.
- Store key-value pairs in nested dictionaries.
- Handle hash collisions without overwriting unrelated entries.
- Add, look up, and safely remove keys.
- Test edge cases and understand dictionary membership.

## 2. Data structure design

The outer dictionary maps a hash value to a bucket. Each bucket is another dictionary containing the original keys and their values.

Example:

```python
{
    412: {
        "dear": "friend",
        "read": "book"
    },
    424: {
        "golf": "sport"
    }
}
```

- Outer key `412`: hash value for both `"dear"` and `"read"`.
- Inner keys `"dear"` and `"read"`: the original keys, kept separate to resolve collisions.
- Inner values: the data associated with each original key.

A hash identifies the bucket, **not necessarily a unique key**.

## 3. The `__init__()` method

```python
def __init__(self):
    self.collection = {}
```

- `__init__` runs when a new instance is created.
- `self` refers to the current instance.
- `self.collection` stores the table's data.
- `{}` creates an empty dictionary.

Create one instance and reuse it:

```python
table = HashTable()
table.add("golf", "sport")
print(table.lookup("golf"))
```

Calling `HashTable()` repeatedly creates separate, empty tables.

## 4. Hashing with `ord()`

The hash method sums the Unicode code point of each character:

```python
def hash(self, key: str) -> int:
    total = 0
    for char in key:
        total += ord(char)
    return total
```

For basic ASCII characters, `ord()` returns the familiar ASCII code. Python supports Unicode too, so “Unicode code point” is the more accurate general term.

For `"golf"`:

| Character | `ord()` result |
|---|---:|
| `g` | 103 |
| `o` | 111 |
| `l` | 108 |
| `f` | 102 |
| **Total** | **424** |

This lab uses the total itself as the outer dictionary key. It does not apply modulo to reduce the hash to a fixed array index.

### Important limitation

Because the algorithm only sums characters, order does not affect the result. For example, `"dear"` and `"read"` both hash to `412`. This makes collision handling essential.

## 5. The `add(key, value)` method

```python
hash_val = self.hash(key)

if hash_val not in self.collection:
    self.collection[hash_val] = {}

self.collection[hash_val][key] = value
```

Step by step:

1. Calculate the key's hash.
2. Check whether the outer dictionary already has that hash.
3. If not, create an empty inner dictionary.
4. Store the original key and value inside the bucket.

The bucket must be created before trying to access `self.collection[hash_val][key]`; otherwise, a missing hash can cause a `KeyError`.

If a different key has the same hash, the existing bucket is reused.

## 6. The `lookup(key)` method

```python
hash_val = self.hash(key)

if hash_val in self.collection and key in self.collection[hash_val]:
    return self.collection[hash_val][key]

return None
```

Two checks are needed:

1. Does the hash bucket exist?
2. Does the original key exist inside that bucket?

Checking only the hash is insufficient because two different keys can collide. The final lookup uses both levels: the hash first, then the original key.

If the key is absent, the method returns `None`, as required.

## 7. The `remove(key)` method

```python
hash_val = self.hash(key)

if hash_val in self.collection and key in self.collection[hash_val]:
    del self.collection[hash_val][key]

    if not self.collection[hash_val]:
        del self.collection[hash_val]
```

The method:

1. Computes the hash.
2. Checks that the bucket exists.
3. Checks that the requested key is in that bucket.
4. Deletes only that key-value pair.
5. Removes the outer bucket if it becomes empty.

This avoids errors when a key is missing. It also protects other keys that share the same hash.

For example, removing `"dear"` from bucket `412` must leave `"read": "book"` untouched.

## 8. Type hints

In `def hash(self, key: str) -> int:`:

- `key: str` is a parameter type annotation.
- `-> int` is a return type annotation.

Type hints document the expected types and help type-checking tools. Python does not automatically enforce them at runtime.

## 9. Testing the requirements

```python
table = HashTable()

assert table.collection == {}
assert table.hash("golf") == 424

table.add("golf", "sport")
assert table.collection[424] == {"golf": "sport"}
assert table.lookup("golf") == "sport"

table.add("dear", "friend")
table.add("read", "book")
assert table.collection[412] == {
    "dear": "friend",
    "read": "book"
}

table.remove("dear")
assert table.lookup("dear") is None
assert table.lookup("read") == "book"

# Removing a missing key should not raise an error.
table.remove("missing")
assert table.lookup("golf") == "sport"

table.add("rose", "flower")
assert table.collection[441] == {"rose": "flower"}

table.add("fcc", "coding")
table.add("cfc", "chemical")
assert table.collection[300] == {
    "fcc": "coding",
    "cfc": "chemical"
}

print("All hash table checks passed.")
```

Run the checks by saving the implementation as `hash_table.py` and running it with Python, or by copying the assertions into a separate test file after importing `HashTable`.

## 10. Complexity

Let `k` be the length of a key and `b` be the number of entries in a bucket.

- Hash calculation: **O(k)**, because every character is visited.
- Bucket access: average **O(1)** for Python dictionaries.
- Inner dictionary insertion, lookup, and deletion: average **O(1)** after hashing, assuming normal dictionary behavior.
- Overall operation: generally **O(k)** because computing the hash takes time proportional to key length.

This is an educational implementation. Production hash tables use more robust hashing strategies and manage their internal storage differently.

## 11. Key takeaways

- `ord()` converts one character into its Unicode code point.
- A hash value identifies a bucket; it does not guarantee a unique key.
- Nested dictionaries let this lab keep colliding keys separate.
- Check existence before deletion to avoid `KeyError`.
- Always check the original key inside the bucket.
- Reuse one table instance when testing multiple operations.
