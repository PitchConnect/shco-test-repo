"""Test assertion errors."""

import pytest
from src.models import BaseModel
from src.utils import validate_list


def test_model_validation():
    """Test model validation."""
    model = BaseModel("test")
    assert model.validate() is True


def test_empty_name_validation():
    """Test validation with empty name."""
    model = BaseModel("")
    assert model.validate() is False


def test_list_validation():
    """Test list validation."""
    assert validate_list([1, 2, 3]) is True
    assert validate_list([]) is False
    assert validate_list("not a list") is False
