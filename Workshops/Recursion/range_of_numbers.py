def range_of_numbers(start_num, end_num):
    """Return every integer from start_num through end_num, inclusive."""
    if start_num == end_num:
        return [start_num]

    return [start_num] + range_of_numbers(start_num + 1, end_num)


if __name__ == "__main__":
    print(range_of_numbers(3, 9))
    print(range_of_numbers(5, 5))
