def print_pattern(n: int):
    """Prints a number pattern starting from n down to 1.

    The function takes one integer parameter and prints the pattern:
    Example if n = 5:

    5 4 3 2 1
    4 3 2 1
    3 2 1
    2 1
    1
    """
    for i in range(n, 0, -1):
        for j in range(i, 0, -1):
            print(j, end=" ")
        print()


# Example usage
print_pattern(5)