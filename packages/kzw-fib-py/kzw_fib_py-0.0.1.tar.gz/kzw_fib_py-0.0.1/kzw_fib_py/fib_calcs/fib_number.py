from typing import Optional

def recurring_fibonacci_number(number: int) -> Optional[int]:
    """Calculates a Fibonacci number

    Args:
        number (int): The number of the Fibonacci number

    Returns:
        Optional[int]: The Fibonacci number
    """
    if number < 0:
        return None
    elif number <= 1:
        return number
    else:
        return recurring_fibonacci_number(number - 1) + recurring_fibonacci_number(number - 2)