"""Tests for type errors."""

import pytest
from src.models import Model
from src.utils import helper_function, validate_list, safe_divide


class TestTypeErrors:
    """Test type error handling."""

    def test_model_name_must_be_string(self):
        """Test that Model raises TypeError for non-string name."""
        with pytest.raises(TypeError, match="name must be a string"):
            Model(123)

    def test_model_value_must_be_int_or_none(self):
        """Test that Model raises TypeError for invalid value type."""
        with pytest.raises(TypeError, match="value must be an integer or None"):
            Model("test", "invalid")

    def test_helper_function_none_raises_type_error(self):
        """Test that helper_function raises TypeError for None."""
        with pytest.raises(TypeError, match="input_data cannot be None"):
            helper_function(None)

    def test_validate_list_non_list_raises_type_error(self):
        """Test that validate_list raises TypeError for non-list."""
        with pytest.raises(TypeError, match="Expected list"):
            validate_list("not a list")

    def test_safe_divide_invalid_numerator(self):
        """Test that safe_divide raises TypeError for invalid numerator."""
        with pytest.raises(TypeError, match="a must be a number"):
            safe_divide("invalid", 2)

    def test_safe_divide_invalid_denominator(self):
        """Test that safe_divide raises TypeError for invalid denominator."""
        with pytest.raises(TypeError, match="b must be a number"):
            safe_divide(10, "invalid")

    def test_safe_divide_by_zero_returns_none(self):
        """Test that safe_divide returns None for division by zero."""
        result = safe_divide(10, 0)
        assert result is None

    def test_safe_divide_valid_inputs(self):
        """Test that safe_divide works with valid inputs."""
        result = safe_divide(10, 2)
        assert result == 5.0

    def test_model_process_none_raises_value_error(self):
        """Test that Model.process raises ValueError for None."""
        model = Model("test")
        with pytest.raises(ValueError, match="data cannot be None"):
            model.process(None)

    def test_model_process_valid_data(self):
        """Test that Model.process works with valid data."""
        model = Model("test")
        result = model.process("data")
        assert result == "data"
