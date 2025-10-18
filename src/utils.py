"""Utility functions."""

from typing import Any, List, Optional


def safe_divide(a: float, b: float) -> Optional[float]:
    """Safely divide two numbers.
    
    Args:
        a: Numerator
        b: Denominator
        
    Returns:
        Result of division or None if division by zero
    """
    if b == 0:
        return None
    return a / b


def validate_list(items: List[Any]) -> bool:
    """Validate a list is not empty.
    
    Args:
        items: List to validate
        
    Returns:
        True if list is valid and not empty
    """
    return isinstance(items, list) and len(items) > 0


def process_data(data: Any) -> str:
    """Process data and return string representation.
    
    Args:
        data: Data to process
        
    Returns:
        String representation of data
    """
    if data is None:
        return "None"
    return str(data)
