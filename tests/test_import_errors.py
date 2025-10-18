"""Tests for import functionality."""

import pytest
import sys
from pathlib import Path


class TestImports:
    """Test import-related functionality."""

    def test_import_models(self):
        """Test that models module can be imported."""
        from src import models
        assert hasattr(models, "Model")

    def test_import_utils(self):
        """Test that utils module can be imported."""
        from src import utils
        assert hasattr(utils, "helper_function")

    def test_import_from_package(self):
        """Test that classes can be imported from package."""
        from src import Model, helper_function
        assert Model is not None
        assert helper_function is not None

    def test_model_class_available(self):
        """Test that Model class is available."""
        from src.models import Model
        instance = Model("test")
        assert instance is not None

    def test_all_exports(self):
        """Test that __all__ exports are correct."""
        import src
        assert hasattr(src, "__all__")
        assert "Model" in src.__all__
        assert "helper_function" in src.__all__
