"""Test type handling."""

import pytest
from src.models import BaseModel
from src.utils import safe_divide, process_data


def test_safe_divide_valid():
    """Test safe division with valid inputs."""
    result = safe_divide(10.0, 2.0)
    assert result == 5.0


def test_safe_divide_by_zero():
    """Test safe division by zero."""
    result = safe_divide(10.0, 0.0)
    assert result is None


def test_process_data_with_none():
    """Test processing None data."""
    result = process_data(None)
    assert result == "None"


def test_process_data_with_string():
    """Test processing string data."""
    result = process_data("test")
    assert result == "test"


def test_process_data_with_number():
    """Test processing numeric data."""
    result = process_data(42)
    assert result == "42"


def test_model_with_different_types():
    """Test model with different value types."""
    model1 = BaseModel("test", 123)
    assert model1.value == 123
    
    model2 = BaseModel("test", "string")
    assert model2.value == "string"
    
    model3 = BaseModel("test", None)
    assert model3.value is None
