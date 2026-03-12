import os

def calculate_average(numbers: list) -> float:
    """Return the arithmetic mean of a list of numbers."""
    if not numbers:
        raise ValueError("Cannot average an empty list.")
    return sum(numbers) / len(numbers)

def get_secret():
    """Get secret from environment variable, never hardcoded."""
    secret = os.getenv("SECRET_KEY")
    if not secret:
        raise EnvironmentError("SECRET_KEY not set.")
    return secret
