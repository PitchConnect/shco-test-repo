"""Tests for assertion errors."""

import pytest
from src.models import Model
from src.utils import helper_function, validate_list


class TestAssertions:
    """Test assertion-related functionality."""

    def test_model_equality(self):
        """Test that models are equal when they have same attributes."""
        model1 = Model("test", 42)
        model2 = Model("test", 42)
        assert model1 == model2

    def test_model_inequality(self):
        """Test that models are not equal when attributes differ."""
        model1 = Model("test1", 42)
        model2 = Model("test2", 42)
        assert model1 != model2

    def test_helper_function_output(self):
        """Test helper function returns correct string."""
        result = helper_function(123)
        assert result == "123"
        assert isinstance(result, str)

    def test_validate_list_empty(self):
        """Test that empty list validation returns False."""
        assert validate_list([]) is False

    def test_validate_list_non_empty(self):
        """Test that non-empty list validation returns True."""
        assert validate_list([1, 2, 3]) is True

    def test_model_value_default(self):
        """Test that model value defaults to 0."""
        model = Model("test")
        assert model.value == 0

    def test_model_value_set(self):
        """Test that model value can be set."""
        model = Model("test", 100)
        assert model.value == 100
