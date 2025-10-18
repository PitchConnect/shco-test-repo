"""Test scenarios for type errors.

Uncomment one test at a time to trigger SHCO fixes.
"""

import pytest
from src.utils import process_data, calculate_sum


# ========== TYPE ERROR 1: Passing string instead of list ==========
# Uncomment to trigger failure
# def test_type_error_1_string_instead_of_list():
#     """Test passing string instead of list."""
#     result = process_data("hello")  # TypeError: object of type 'str' has no len()
#     assert result == 5


# ========== TYPE ERROR 2: Passing int instead of list ==========
# Uncomment to trigger failure
# def test_type_error_2_int_instead_of_list():
#     """Test passing int instead of list."""
#     result = calculate_sum(123)  # TypeError: 'int' object is not iterable
#     assert result == 6


# ========== TYPE ERROR 3: Wrong return type ==========
# Uncomment to trigger failure
# def test_type_error_3_wrong_return_type():
#     """Test function with wrong return type."""
#     def get_number() -> str:  # Type hint says str
#         return 42  # But returns int
#     
#     result = get_number()
#     # This won't fail at runtime, but type checkers will complain
#     assert result == 42


# ========== TYPE ERROR 4: Missing required parameter ==========
# Uncomment to trigger failure
# def test_type_error_4_missing_parameter():
#     """Test calling function without required parameter."""
#     from src.models import User
#     user = User("Alice")  # TypeError: __init__() missing 1 required positional argument: 'age'
#     assert user.get_name() == "Alice"


# ========== TYPE ERROR 5: Extra unexpected parameter ==========
# Uncomment to trigger failure
# def test_type_error_5_extra_parameter():
#     """Test calling function with extra parameter."""
#     result = calculate_sum([1, 2, 3], reverse=True)  # TypeError: calculate_sum() got an unexpected keyword argument 'reverse'
#     assert result == 6


# Placeholder test to keep pytest happy
def test_placeholder():
    """Placeholder test."""
    assert True

