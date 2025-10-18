"""Test scenarios for import errors.

Uncomment one test at a time to trigger SHCO fixes.
"""

import pytest


# ========== IMPORT ERROR 1: Missing User import ==========
# Uncomment to trigger failure
def test_import_error_1_missing_user():
    """Test missing User import - triggers NameError (test 7 - with logging)."""
    user = User("Alice", 30)  # NameError: name 'User' is not defined
    assert user.get_name() == "Alice"


# ========== IMPORT ERROR 2: Missing Database import ==========
# Uncomment to trigger failure
# def test_import_error_2_missing_database():
#     """Test missing Database import."""
#     db = Database()  # NameError: name 'Database' is not defined
#     assert db.connect() is True


# ========== IMPORT ERROR 3: Missing Config import ==========
# Uncomment to trigger failure
# def test_import_error_3_missing_config():
#     """Test missing Config import."""
#     config = Config()  # NameError: name 'Config' is not defined
#     assert config.get_config()["debug"] is True


# ========== IMPORT ERROR 4: Wrong import path for utils ==========
# Uncomment to trigger failure
# def test_import_error_4_wrong_path():
#     """Test wrong import path."""
#     from utils import get_items  # ImportError: No module named 'utils'
#     items = get_items()
#     assert len(items) == 3


# ========== IMPORT ERROR 5: Missing datetime import ==========
# Uncomment to trigger failure
# def test_import_error_5_missing_datetime():
#     """Test missing datetime import in utils."""
#     from src.utils import format_date
#     # This will fail because utils.py uses datetime without importing it
#     date_str = format_date(1234567890)  # NameError in utils.py
#     assert isinstance(date_str, str)


# Placeholder test to keep pytest happy
def test_placeholder():
    """Placeholder test."""
    assert True

