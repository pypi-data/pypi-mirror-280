from typing import List

from .fib_number import recurring_fibonacci_number

def calculate_numbers(numbers: List[int]) -> List[int]:
    """Calculates Fibonacci numbers

    Args:
        numbers (List[int]): The numbers of the Fibonacci numbers

    Returns:
        List[int]: The Fibonacci numbers
    """
    return [recurring_fibonacci_number(number=i) for i in numbers]
