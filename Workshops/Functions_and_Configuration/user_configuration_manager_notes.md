# Workshop Notes — User Configuration Manager

## Goal
Manage key-value settings in a dictionary with functions to add, update, delete, and display settings.

## Concepts
- A dictionary stores values under unique keys.
- `.lower()` normalizes keys and values to lowercase.
- `in` checks whether a key exists.
- Assignment adds or updates a dictionary entry.
- `del settings[key]` removes an existing entry.
- `.items()` iterates over key-value pairs.
- `.capitalize()` formats a key for display.
- Functions return status messages so callers can display or test the result.

## Functions
- `add_setting(settings, setting)`: refuses duplicate keys.
- `update_setting(settings, setting)`: changes an existing key only.
- `delete_setting(settings, key)`: removes a setting if found.
- `view_settings(settings)`: returns a readable summary or an empty-state message.

## Important notes
- The `setting` argument for add/update is expected to be a two-item iterable such as `("theme", "light")`.
- The code lowercases values as well as keys. That is appropriate for these simple settings but would not suit every possible configuration value.
- The file contains freeCodeCamp wrapper markers that are not Python syntax; preserve them for the exercise, or remove them in a separate standalone copy.

## Practice
Try adding a new setting, updating an existing one, deleting a missing key, and viewing an empty dictionary.
