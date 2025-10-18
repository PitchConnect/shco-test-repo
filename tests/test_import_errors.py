"""Test import functionality."""

import pytest


def test_import_models():
    """Test that models module can be imported."""
    from src import models
    assert hasattr(models, "BaseModel")


def test_import_utils():
    """Test that utils module can be imported."""
    from src import utils
    assert hasattr(utils, "safe_divide")
    assert hasattr(utils, "validate_list")
    assert hasattr(utils, "process_data")


def test_import_base_model():
    """Test that BaseModel can be imported directly."""
    from src.models import BaseModel
    assert BaseModel is not None
