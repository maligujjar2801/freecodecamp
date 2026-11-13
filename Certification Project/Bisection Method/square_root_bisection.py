def square_root_bisection(square_target, tolerance=0.01, maximum=100):
    if square_target < 0:
        raise ValueError(
            "Square root of negative number is not defined in real numbers"
        )

    if square_target == 0 or square_target == 1:
        print(f"The square root of {square_target} is {square_target}")
        return square_target

    lower = 0
    upper = max(1, square_target)

    for _ in range(maximum):
        root = (lower + upper) / 2
        root_squared = root ** 2

        if root_squared == square_target:
            print(
                f"The square root of {square_target} is approximately {root}"
            )
            return root

        if root_squared < square_target:
            lower = root
        else:
            upper = root

        if upper - lower <= tolerance:
            root = (lower + upper) / 2
            print(
                f"The square root of {square_target} is approximately {root}"
            )
            return root

    print(f"Failed to converge within {maximum} iterations")
    return None


if __name__ == "__main__":
    square_root_bisection(81, 1e-3, 50)
    square_root_bisection(225, 1e-3, 100)
    square_root_bisection(225, 1e-7, 10)
    square_root_bisection(0.001, 1e-7, 50)
    square_root_bisection(0.25, 1e-7, 50)
