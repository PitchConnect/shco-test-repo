"""Utility functions."""

from typing import Any, List, Optional


def helper_function(input_data: Any) -> str:
    """Helper function to process input data.
    
    Args:
        input_data: Data to process
        
    Returns:
        String representation of the data
        
    Raises:
        TypeError: If input_data is None
    """
    if input_data is None:
        raise TypeError("input_data cannot be None")
    return str(input_data)


def validate_list(items: List[Any]) -> bool:
    """Validate a list of items.
    
    Args:
        items: List to validate
        
    Returns:
        True if valid, False otherwise
    """
    if not isinstance(items, list):
        raise TypeError(f"Expected list, got {type(items).__name__}")
    return len(items) > 0


def safe_divide(a: float, b: float) -> Optional[float]:
    """Safely divide two numbers.
    
    Args:
        a: Numerator
        b: Denominator
        
    Returns:
        Result of division or None if division by zero
    """
    if not isinstance(a, (int, float)):
        raise TypeError(f"a must be a number, got {type(a).__name__}")
    if not isinstance(b, (int, float)):
        raise TypeError(f"b must be a number, got {type(b).__name__}")
    
    if b == 0:
        return None
    return a / b
