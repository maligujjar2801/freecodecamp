class HashTable:
    """A simple hash table that handles collisions with nested dictionaries."""

    def __init__(self):
        self.collection = {}

    def hash(self, key: str) -> int:
        """Return the sum of the Unicode code points in key."""
        total = 0
        for char in key:
            total += ord(char)
        return total

    def add(self, key, value):
        """Add or update a key-value pair in its hash bucket."""
        hash_val = self.hash(key)

        # Create the bucket only when this hash has not been used yet.
        if hash_val not in self.collection:
            self.collection[hash_val] = {}

        # Keep the original key inside the bucket to handle collisions.
        self.collection[hash_val][key] = value

    def remove(self, key):
        """Remove a key if it exists; otherwise, do nothing."""
        hash_val = self.hash(key)

        if (
            hash_val in self.collection
            and key in self.collection[hash_val]
        ):
            del self.collection[hash_val][key]

            # Avoid keeping an empty bucket in the outer dictionary.
            if not self.collection[hash_val]:
                del self.collection[hash_val]

    def lookup(self, key):
        """Return a key's value, or None if the key is absent."""
        hash_val = self.hash(key)

        if (
            hash_val in self.collection
            and key in self.collection[hash_val]
        ):
            return self.collection[hash_val][key]

        return None


if __name__ == "__main__":
    table = HashTable()

    table.add("golf", "sport")
    table.add("dear", "friend")
    table.add("read", "book")

    print("Hash of 'golf':", table.hash("golf"))  # 424
    print("Lookup 'golf':", table.lookup("golf"))  # sport
    print("Collision bucket (412):", table.collection[412])
    # {'dear': 'friend', 'read': 'book'}

    table.remove("dear")
    print("Lookup 'dear' after removal:", table.lookup("dear"))  # None
    print("Lookup 'read' after removing 'dear':", table.lookup("read"))  # book
