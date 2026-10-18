# Workshop Notes — Build a Range of Numbers Generator

## Goal

Write a recursive function named `range_of_numbers(start_num, end_num)` that returns a list of every consecutive integer from `start_num` through `end_num`, including both endpoints.

Examples:

```python
range_of_numbers(3, 9)  # [3, 4, 5, 6, 7, 8, 9]
range_of_numbers(5, 5)  # [5]
```

The lab guarantees that `start_num <= end_num`.

## Complete solution

```python
def range_of_numbers(start_num, end_num):
    if start_num == end_num:
        return [start_num]

    return [start_num] + range_of_numbers(start_num + 1, end_num)
```

## Concepts used

- **Recursion:** A function calls itself to solve a smaller version of the same problem.
- **Base case:** The condition that stops further recursive calls.
- **Recursive case:** The part that calls the function again with a value closer to the base case.
- **Lists:** Square brackets, such as `[start_num]`, create a list containing one item.
- **List concatenation:** The `+` operator combines lists. For example, `[3] + [4, 5]` becomes `[3, 4, 5]`.
- **Return values:** Each call returns a list to the call that invoked it.
- **Call stack:** Python keeps track of unfinished calls until the base case returns.

## Understand the base case

```python
if start_num == end_num:
    return [start_num]
```

When the start and end values are equal, there is only one number to include. Return it inside a list.

For example, `range_of_numbers(5, 5)` returns `[5]`, not `5`. The square brackets are important because the function must always return a list.

Without a base case, the function would keep calling itself until Python raises a recursion-depth error.

## Understand the recursive case

```python
return [start_num] + range_of_numbers(start_num + 1, end_num)
```

This expression does three things:

1. Wraps the current `start_num` in a one-item list.
2. Calls the same function with `start_num + 1`, moving toward `end_num`.
3. Joins the one-item list to the list returned by the recursive call.

The recursive call does not return a single number. It returns a list, so list concatenation produces one combined list.

Example of concatenation:

```python
[3] + [4, 5, 6]
# [3, 4, 5, 6]
```

## Trace the calls

Consider `range_of_numbers(3, 6)`.

### Going down into recursive calls

```text
range_of_numbers(3, 6)
    [3] + range_of_numbers(4, 6)
              [4] + range_of_numbers(5, 6)
                        [5] + range_of_numbers(6, 6)
                                  returns [6]
```

Each call increases `start_num` by one. When the call reaches `range_of_numbers(6, 6)`, the base case returns `[6]`.

### Returning back up

```text
range_of_numbers(6, 6) returns [6]
range_of_numbers(5, 6) returns [5] + [6]       -> [5, 6]
range_of_numbers(4, 6) returns [4] + [5, 6]    -> [4, 5, 6]
range_of_numbers(3, 6) returns [3] + [4, 5, 6] -> [3, 4, 5, 6]
```

Final result:

```python
[3, 4, 5, 6]
```

The calls reach the base case first; then their return values are combined while the call stack unwinds.

## Why does it return a list rather than separate numbers?

The base case returns a list: `[start_num]`. Every recursive call also returns a list. The `+` operator joins those lists into a single flat list.

Compare these expressions:

```python
return start_num       # one integer
return [start_num]     # a list with one integer
return [start_num] + [start_num + 1]  # a combined list
```

The function never needs a global list. Each call creates and returns its own result, and the caller combines that result with its current number.

## User-story checklist

1. **Function name and parameters:** `range_of_numbers(start_num, end_num)`.
2. **Inclusive consecutive values:** Both endpoints appear in the returned list.
3. **Input order:** The lab guarantees `start_num <= end_num`.
4. **Uses recursion:** The function calls `range_of_numbers()` from inside itself.
5. **No loops or built-in range:** The solution uses no `for`, `while`, comprehension, or `range()`.
6. **Base case:** Equal values return `[start_num]`.
7. **Progress toward the base case:** `start_num + 1` moves closer to `end_num`.
8. **No global result list:** The result is passed back through return values.

## Test the function

```python
print(range_of_numbers(3, 9))
# [3, 4, 5, 6, 7, 8, 9]

print(range_of_numbers(5, 5))
# [5]

print(range_of_numbers(1, 3))
# [1, 2, 3]

print(range_of_numbers(8, 10))
# [8, 9, 10]
```

## Common mistakes

- **Returning `start_num` instead of `[start_num]`:** This makes the base case return an integer instead of a list.
- **Forgetting to return the recursive expression:** Without `return`, the caller receives `None`.
- **Not changing the argument:** Calling the function with the same values never moves toward the base case.
- **Moving in the wrong direction:** Increasing `start_num` is correct because the base case is reached when it equals `end_num`.
- **Using a loop or `range()`:** The lab explicitly prohibits these.
- **Using a global list:** Each call should return its own list rather than relying on shared global state.

## Complexity

Let `n = end_num - start_num + 1`, the number of integers returned.

- **Recursive call depth:** `O(n)`, because the function makes one call per number.
- **Time complexity:** `O(n²)` for this particular implementation, because list concatenation copies the accumulated list at each return step.
- **Output size:** `O(n)` integers.

This implementation is clear for learning recursion. For very large ranges, Python's recursion-depth limit is another practical constraint.

## Practice

Before running these examples, predict their output:

```python
range_of_numbers(2, 4)
range_of_numbers(7, 7)
range_of_numbers(1, 5)
```

Then explain in your own words:

1. Why does the base case return a list?
2. How does `start_num + 1` move the function toward the base case?
3. What does list concatenation do when the recursive call returns `[3, 4]` and the current call has `start_num == 2`?

**Key takeaway:** Recursion builds the answer by reaching a simple base case first, then combining each pending call's current number with the list returned from deeper calls.
