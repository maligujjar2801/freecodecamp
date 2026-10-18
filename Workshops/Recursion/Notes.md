# Python Workshop — Recursion: Count Up

## 1. Code

```python
def countup(number):
    if number < 1:
        return []

    count_list = countup(number - 1)
    count_list.append(number)
    return count_list
```

## 2. Concepts Used

- **Recursion:** A function calls itself to solve a smaller version of the same problem.
- **Base case:** `if number < 1: return []` stops the recursion.
- **Recursive case:** `countup(number - 1)` calls the function with a smaller number.
- **List:** `append(number)` adds the current number to the list.
- **Return:** `return count_list` sends the completed list back to the caller.

## 3. How It Works

Example: `countup(3)`

1. `countup(3)` calls `countup(2)`.
2. `countup(2)` calls `countup(1)`.
3. `countup(1)` calls `countup(0)`.
4. `countup(0)` returns an empty list `[]` because the base case is reached.
5. The functions resume and append their numbers in order: `1`, `2`, then `3`.

**Output:**

```python
print(countup(3))
# [1, 2, 3]
```

## 4. Important Lesson

The function first goes down through recursive calls. Once it reaches the base case, it returns back up the call stack, appending each number along the way.

This is why the result is `[1, 2, 3]`, not `[3, 2, 1]`.

## 5. Complexity

- **Time complexity:** O(n)
- **Space complexity:** O(n), including the result list and recursion call stack.

## 6. Practice

Predict the output:

```python
print(countup(5))
```

Expected output:

```python
[1, 2, 3, 4, 5]
```

**Remember:** Every recursive function needs a stopping condition to prevent infinite recursion.