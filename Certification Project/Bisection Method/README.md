# Bisection Method — Square Root Approximation

A no-import Python implementation of the bisection method, built for the freeCodeCamp **Implement the Bisection Method** lab.

## Files

- **square_root_bisection.py** — the function and five runnable examples.
- **detailed_notes.md** — the mathematical model, the reason behind each decision, line-by-line code explanations, and test coverage.

## Run

Requires Python 3. Save the project folder, open a terminal inside it, and run:

~~~bash
python square_root_bisection.py
~~~

To use the function in another Python file:

~~~python
from square_root_bisection import square_root_bisection

result = square_root_bisection(225, tolerance=1e-7, maximum=100)
print(result)
~~~

The implementation itself imports **no modules**.

## Algorithm

1. Reject negative targets and return 0 or 1 directly.
2. Start with an interval that contains the square root.
3. Calculate the midpoint and compare its square with the target.
4. Keep the half-interval that still contains the answer.
5. Return the final midpoint when the interval width is within the tolerance.
6. Return **None** with the required failure message when the iteration limit is reached first.

## Verification

All **23 checks represented by the lab checklist supplied with this project** were reproduced locally and passed, including the required return values, printed messages, negative-input exception, and maximum-iteration failure case.

See **detailed_notes.md** for the complete conceptual and line-by-line explanation.
