import random  # Importing Python's built-in random module to generate random numbers


def add(x: int, y: int) -> int:
    """
    Adds two numbers together.

    Args:
        x (int): The first number.
        y (int): The second number.

    Returns:
        int: The sum of x and y.
    """
    return x + y  # Return the sum of the two numbers


def is_large_number(x: int) -> bool:
    """
    Determines if a number is considered 'large' (7 or higher).

    Args:
        x (int): The number to check.

    Returns:
        bool: True if x is 7 or greater, otherwise False.
    """
    if x >= 7:
        return True  # Number is large
    else:
        return False  # Number is not large

if __name__ == "__main__":
    # Generate two random integers between 0 and 10
    num1: int = random.randint(0, 10)
    num2: int = random.randint(0, 10)

    # Print the two randomly generated numbers
    print(num1, num2)

    # Example without using a function
    print(num1 + num2)  # Adds the numbers directly

    # Example using the function
    print(add(num1, num2))  # Uses the 'add' function for the same result

    # Example without using a function
    if num1 >= 7:
        is_large: bool = True
    else:
        is_large = False

    print(is_large)  # Shows if num1 is large (manual logic)

    # Example using the function
    print(is_large_number(num2))  # Uses the 'is_large_number' function for cleaner code
