# Binary Search — Workshop Notes

## Goal

Implement **binary search**, an efficient algorithm for finding a value in a **sorted list**. This implementation also records the values inspected along the way, so you can see the search path.

## The key idea

Instead of checking every element from left to right, binary search repeatedly checks the middle of the remaining search range.

1. Find the middle index.
2. Compare the middle value with the target.
3. If they match, return the values inspected so far.
4. If the target is larger, discard the left half by moving `low` to `mid + 1`.
5. If the target is smaller, discard the right half by moving `high` to `mid - 1`.
6. Repeat while `low <= high`. If the range becomes empty, the target is not present.

**Important:** the list must be sorted in ascending order for these comparisons to work correctly.

## Understanding the code

### 1. Track the search path

```python
path_to_target = []
```

This empty list stores each middle value inspected. It makes the algorithm's decisions visible and is useful for learning and debugging.

### 2. Define the current search range

```python
low = 0
high = len(search_list) - 1
```

- `low` is the first index that could still contain the target.
- `high` is the last index that could still contain the target.
- `len(search_list) - 1` gives the final valid index because Python indexing starts at zero.

### 3. Continue while the range exists

```python
while low <= high:
```

The range is valid as long as `low` is not greater than `high`. If `low > high`, there are no candidates left.

### 4. Find the middle

```python
mid = (low + high) // 2
value_at_middle = search_list[mid]
path_to_target.append(value_at_middle)
```

The `//` operator performs floor division, producing an integer index. The algorithm checks the value at that index and records it in the path.

### 5. Compare the middle value with the target

```python
if value == value_at_middle:
    return path_to_target
elif value > value_at_middle:
    low = mid + 1
else:
    high = mid - 1
```

- **Equal:** the target was found, so return the search path.
- **Target is greater:** every value at or to the left of the middle can be ruled out, so continue at `mid + 1`.
- **Target is smaller:** every value at or to the right of the middle can be ruled out, so continue at `mid - 1`.

The `+ 1` and `- 1` are essential: they prevent the already-checked middle index from remaining in the search range.

### 6. Handle a missing target

```python
return [], "Value not found"
```

This returns a **tuple** containing an empty list and a message—not just a list. That means the function has different return shapes for success and failure. For a more consistent API, you could instead return `None` or return a pair such as `(False, path_to_target)`. This workshop keeps the supplied implementation unchanged so you can study its behavior.

## Trace the supplied examples

### Example 1

```python
binary_search([1, 2, 3, 4, 5], 3)
```

- Middle index: `(0 + 4) // 2 = 2`
- Middle value: `3`
- The target matches immediately.

Result: `[3]`

### Example 2

```python
binary_search([1, 2, 3, 4, 5, 9], 4)
```

- Start with indices `0` through `5`; middle index is `2`, value `3`. Path: `[3]`.
- The target `4` is greater, so set `low = 3`.
- The remaining middle index is `(3 + 5) // 2 = 4`, value `5`. Path: `[3, 5]`.
- The target `4` is smaller, so set `high = 3`.
- The remaining middle index is `(3 + 3) // 2 = 3`, value `4`. Found.

Result: `[3, 5, 4]`

### Example 3

```python
binary_search([1, 3, 5, 9, 14, 22], 10)
```

- Check `5`; target is greater. Path: `[5]`.
- Check `14`; target is smaller. Path: `[5, 14]`.
- Check `9`; target is greater. Path: `[5, 14, 9]`.
- The remaining range is empty, so the target is not found.

Result: `([], "Value not found")`

## Complexity

- **Time:** (O(\log n)) in the average and worst cases for a sorted list, because the remaining search range is approximately halved each iteration.
- **Extra space:** (O(\log n)) for this version's `path_to_target` list in the worst case. A version that does not store the path uses (O(1)) extra space.

## Common mistakes

- Using binary search on an unsorted list.
- Updating `low = mid` or `high = mid` instead of moving past the middle with `mid + 1` or `mid - 1`.
- Using `<` where the loop needs `<=`, which can skip a final remaining element.
- Forgetting that `mid` is an index, while `search_list[mid]` is the value.
- Assuming the failure return is a list; the provided code returns a tuple on failure.

## Practice tasks

1. Trace the path when searching for `1` in `[1, 2, 3, 4, 5]`.
2. Trace the path when searching for `5` in the same list.
3. Try an empty list and describe what the function returns.
4. Modify the function so both success and failure use one consistent return format.
5. Add a test for a value smaller than the first item and one larger than the last item.

## Coding flow

**Understand → Trace → Run → Test edge cases → Explain → Commit.**

Before moving on, make sure you can explain why each comparison discards half of the remaining range and why the list must be sorted.
