# Bisection Method — Detailed Notes

## 1. Project goal

The task is to write a function named `square_root_bisection` that approximates the square root of a non-negative number without importing a module.

The function accepts three parameters:

- `square_target`: the number whose square root is being found.
- `tolerance`: the accepted maximum width of the remaining search interval. The default is **0.01**.
- `maximum`: the maximum number of bisection iterations. The default is **100**.

The function must also follow the exact messages and return behaviour required by the freeCodeCamp lab.

## 2. The mathematical model

Finding the square root of a number is equivalent to finding a value $x$ that satisfies:

$$
x^2 = T
$$

We can rearrange this as a root-finding problem:

$$
f(x) = x^2 - T = 0
$$

The bisection method does not need to guess the answer directly. It keeps an interval containing the answer and repeatedly cuts that interval in half.

### Why the interval works

For every positive target:

- The lower boundary starts at **0**. Its square is **0**, which is below the positive target.
- The upper boundary is chosen so its square is at least the target:
  - For a target greater than or equal to **1**, the upper boundary is the target itself.
  - For a target between **0** and **1**, the upper boundary is **1**.

Therefore, the square root is inside the interval.

For example, when the target is **225**, the square root is **15**, and the initial interval is:

$$
0 \leq \sqrt{225} \leq 225
$$

When the target is **0.25**, the square root is **0.5**, and the initial interval is:

$$
0 \leq \sqrt{0.25} \leq 1
$$

The interval may be much wider than necessary at the beginning. That is fine: bisection progressively narrows it.

## 3. The midpoint decision — the heart of the algorithm

Calculate the midpoint:

$$
m = \frac{L+U}{2}
$$

Then square it and compare the result with the target.

| Comparison | Meaning | Correct update |
|---|---|---|
| $m^2 < T$ | The midpoint is below the positive square root. | Move the lower boundary up to $m$. |
| $m^2 > T$ | The midpoint is above the positive square root. | Move the upper boundary down to $m$. |
| $m^2 = T$ | The exact square root has been found. | Return the midpoint immediately. |

**The comparison directions are important:** a midpoint that is too small moves the lower boundary up; a midpoint that is too large moves the upper boundary down.

### Example: finding the square root of 25

Start with the interval $[0,25]$.

| Step | Midpoint | Midpoint squared | Decision | Remaining interval |
|---:|---:|---:|---|---|
| 1 | 12.5 | 156.25 | Too large | [0, 12.5] |
| 2 | 6.25 | 39.0625 | Too large | [0, 6.25] |
| 3 | 3.125 | 9.765625 | Too small | [3.125, 6.25] |
| 4 | 4.6875 | 21.97265625 | Too small | [4.6875, 6.25] |
| 5 | 5.46875 | 29.9072265625 | Too large | [4.6875, 5.46875] |

Each comparison discards the half that cannot contain the answer. The interval keeps shrinking around **5**.

## 4. What tolerance actually means

The interval width is:

$$
\text{width} = U - L
$$

The algorithm checks whether:

$$
U - L \leq \varepsilon
$$

When this condition becomes true, the search interval is sufficiently narrow, so the function returns its midpoint.

Because the true answer is still inside the interval, the distance from its midpoint to the answer cannot exceed half the interval width. Therefore, when the width is at most the tolerance, the midpoint's absolute error is at most half the tolerance.

**Tolerance is not the number of iterations.** It controls the accepted interval width. The maximum parameter controls how many times the algorithm is allowed to narrow the interval.

### Why the 10-iteration example must fail

For a target of **225**, the starting interval has width **225**. After 10 bisections, its width is:

$$
\frac{225}{2^{10}} \approx 0.2197
$$

That is still greater than $10^{-7}$. The algorithm must therefore print the failure message and return **None**, exactly as the lab expects.

## 5. Why the original loop was simplified

The comparison directions in the submitted code were correct. The difficult part was the repeated midpoint recalculation inside the conditional branches.

The original version could:

1. Calculate one midpoint.
2. Change a boundary.
3. Calculate another midpoint inside that branch.
4. Compare that newly calculated midpoint in a second independent **if** statement.
5. Potentially change the other boundary during the same outer-loop iteration.

That makes it harder to track what one iteration means and why the interval changed.

The revised version uses one consistent cycle:

1. Calculate one midpoint.
2. Compare its square with the target.
3. Update exactly one boundary, unless the answer is exact.
4. Check the updated interval width.
5. Start the next iteration if more precision is needed.

The next midpoint is calculated at the top of the next loop iteration. This keeps the algorithm easier to reason about and makes the iteration limit predictable.

## 6. Code explained line by line

The line numbers below match the non-empty lines in `square_root_bisection.py`.

| Line | Code or code block | Explanation |
|---:|---|---|
| 1 | `def square_root_bisection(square_target, tolerance=0.01, maximum=100):` | Defines the function with exactly three parameters. The two optional parameters have default values, so the caller can supply only the target or override the precision and iteration limit. |
| 2 | `if square_target < 0:` | Checks whether the target is negative. A negative number has no real-valued square root. |
| 3–5 | **raise ValueError(...)** | Stops execution and raises the required exception with the exact message specified by the lab. The message is split across lines only to keep the source readable. |
| 7 | `if square_target == 0 or square_target == 1:` | Checks the two special inputs whose square roots are already known exactly. |
| 8 | **print(...)** | Prints the special-case message. It deliberately says “is” rather than “is approximately”, matching the user story. |
| 9 | `return square_target` | Returns the input itself. Both $0^2=0$ and $1^2=1$. Returning also ends the function immediately. |
| 11 | **lower = 0** | Establishes the lowest possible starting boundary for the positive square root. |
| 12 | `upper = max(1, square_target)` | Chooses an upper boundary that contains the square root for targets below or above $1$. The built-in **max** function is not an imported module. |
| 14 | `for _ in range(maximum):` | Repeats the bisection process no more than the allowed number of times. The underscore means the loop counter is not needed in the algorithm. |
| 15 | **root = (lower + upper) / 2** | Finds the midpoint of the current interval. This is the current candidate for the square root. |
| 16 | `root_squared = root ` 2** | Squares the candidate. Python's power operator squares the candidate, calculating it multiplied by itself. |
| 18 | `if root_squared == square_target:` | Checks whether the midpoint is an exact solution. This is an optional early exit; the tolerance check is still needed because many square roots are not reached exactly in floating-point arithmetic. |
| 19–21 | **print(...)** | Prints the required approximate-result message. The f-string inserts the actual target and candidate value into the message. |
| 22 | **return root** | Returns the exact midpoint and stops the function when the equality check succeeds. |
| 24 | `if root_squared < square_target:` | Checks whether the midpoint is too small. Squaring a non-negative number preserves its order, so a square below the target means the midpoint is below the square root. |
| 25 | **lower = root** | Discards the lower half of the interval by moving the lower boundary to the midpoint. The answer must be above this candidate. |
| 26 | **else:** | Handles the remaining comparison case. Exact equality has already returned, so this branch means the squared midpoint is greater than the target. |
| 27 | **upper = root** | Discards the upper half of the interval by moving the upper boundary down to the midpoint. |
| 29 | **if upper - lower <= tolerance:** | Checks the width of the newly updated interval. The algorithm stops when the interval is sufficiently narrow. |
| 30 | **root = (lower + upper) / 2** | Calculates the midpoint of the final, narrowed interval. This is the best candidate to return from the remaining bracket. |
| 31–33 | **print(...)** | Prints the approximate-result message using the final midpoint. |
| 34 | **return root** | Returns the approximation and ends the function once the tolerance requirement is satisfied. |
| 36 | **print(...)** | This line is reached only when the loop finishes without finding an exact result or a sufficiently narrow interval. It prints the required failure message. |
| 37 | **return None** | Indicates that the function did not achieve the requested tolerance within the permitted iterations. |
| 40 | `if __name__ == "__main__":` | Runs the examples only when this file is executed directly. If another Python file imports the function, these demonstrations do not run automatically. |
| 41 | `square_root_bisection(81, 1e-3, 50)` | Tests an integer target with a tolerance of $10^{-3}$ and a 50-iteration limit. |
| 42 | `square_root_bisection(225, 1e-3, 100)` | Tests a larger perfect square with a 100-iteration limit. |
| 43 | `square_root_bisection(225, 1e-7, 10)` | Deliberately tests insufficient iterations. It should print the failure message and return **None**. |
| 44 | `square_root_bisection(0.001, 1e-7, 50)` | Tests a small positive target below $1$, checking that the initial upper bound is chosen correctly. |
| 45 | `square_root_bisection(0.25, 1e-7, 50)` | Tests another target below $1$. The exact midpoint $0.5$ can be found during the search. |

## 7. Important Python ideas used

### Default parameters

In the function definition:

~~~python
def square_root_bisection(square_target, tolerance=0.01, maximum=100):
~~~

A call such as `square_root_bisection(25)` uses both defaults. A call such as `square_root_bisection(25, 1e-7, 50)` overrides them.

### The exponentiation operator

~~~python
root_squared = root ** 2
~~~

This means “root raised to the power of two.” It is not the same as multiplying by two.

### The max built-in

~~~python
upper = max(1, square_target)
~~~

It returns whichever of the two values is greater. It is a built-in Python function, so no import is needed.

### The return statement

A **return** statement immediately exits the function and sends a value back to the caller. A **print** statement only displays text; it does not replace the return value.

That is why the function prints the required message and separately returns the numerical result.

### The None value

**None** represents the absence of a successful numerical result in the iteration-limit failure case. It is different from printing the word “None”.

## 8. Test coverage

The implementation was checked locally against all 23 checks represented in the lab checklist supplied for this project.

| Requirement area | Verification |
|---|---|
| No module imports | Passed |
| Function name and three parameters | Passed |
| Default tolerance and maximum | Passed |
| Negative input and exact ValueError message | Passed |
| Target 0 return value and print message | Passed |
| Target 1 return value and print message | Passed |
| Target 0.001 at tolerance $10^{-7}$ | Passed |
| Target 0.25 at tolerance $10^{-7}$ | Passed |
| Target 81 at tolerance $10^{-3}$ | Passed |
| Target 225 at tolerances $10^{-3}$, $10^{-5}$, and $10^{-7}$ | Passed |
| Target 225 with only 10 iterations | Passed — returns **None** and prints the required failure message |

These are local reproductions of the supplied assertions. They do not represent a submission to or a live result from the freeCodeCamp website.

## 9. Complexity

Let $W$ be the initial interval width and $n$ the number of iterations.

- **Time complexity:** $O(n)$. Each iteration performs a constant number of arithmetic operations and comparisons.
- **Space complexity:** $O(1)$. The function stores only a fixed number of variables.
- **Interval reduction:** Each completed bisection halves the interval width.

The method is efficient because it reduces the uncertainty exponentially with respect to the number of iterations.

## 10. Final conceptual takeaway

The key idea is not “keep guessing numbers until one looks correct.”

It is:

1. Establish an interval that is guaranteed to contain the answer.
2. Test the midpoint.
3. Use the comparison to prove which half cannot contain the answer.
4. Discard that half.
5. Repeat until the remaining interval is sufficiently narrow.

**Every comparison should preserve the root inside the remaining interval.** That invariant is the reason bisection works.
