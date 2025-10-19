# Week 4, Session 2: Task 3

# Given incomplete function sum_all with a docstring, your
# task is to complete the function based on the details
# in the docstring.


def sum_all(*args):
    """
    This function accepts an arbitrary number of arguments and returns their
    sum. It only sums numeric arguments (integers or floats), ignoring
    non-numeric values.

    Args:
        *args: Arbitrary positional arguments of any type.

    Returns:
        float: The sum of all numeric arguments.
    """

    # complete your code here

    return sum


# Check if correct output is produced
print(sum_all(1, 2, 3, 4, 5))    # Output: 15
print(sum_all(10, "apple", 20, 30, 1.5))  # Output: 61.5
print(sum_all())  # Output: 0
