"""Test scenarios for assertion errors.

Uncomment one test at a time to trigger SHCO fixes.
"""

import pytest
from src.models import User, Database, Config
from src.utils import get_items


# ========== ASSERTION ERROR 1: Wrong expected count ==========
# Uncomment to trigger failure
# def test_assertion_error_1_wrong_count():
#     """Test wrong expected count."""
#     db = Database()
#     count = db.count_users()
#     assert count == 5  # AssertionError: assert 4 == 5


# ========== ASSERTION ERROR 2: Wrong expected string ==========
# Uncomment to trigger failure
# def test_assertion_error_2_wrong_string():
#     """Test wrong expected string."""
#     user = User("Alice", 30)
#     name = user.get_name()
#     assert name == "Bob"  # AssertionError: assert 'Alice' == 'Bob'


# ========== ASSERTION ERROR 3: Wrong expected list length ==========
# Uncomment to trigger failure
# def test_assertion_error_3_wrong_length():
#     """Test wrong expected list length."""
#     items = get_items()
#     assert len(items) == 5  # AssertionError: assert 3 == 5


# ========== ASSERTION ERROR 4: Wrong expected boolean ==========
# Uncomment to trigger failure
# def test_assertion_error_4_wrong_boolean():
#     """Test wrong expected boolean."""
#     user = User("Alice", 30)
#     active = user.is_active()
#     assert active is False  # AssertionError: assert True is False


# ========== ASSERTION ERROR 5: Wrong expected dict keys ==========
# Uncomment to trigger failure
# def test_assertion_error_5_wrong_dict():
#     """Test wrong expected dict keys."""
#     config = Config()
#     settings = config.get_config()
#     assert "timeout" in settings  # AssertionError: assert 'timeout' in {'debug': True, 'port': 8000}


# Placeholder test to keep pytest happy
def test_placeholder():
    """Placeholder test."""
    assert True

