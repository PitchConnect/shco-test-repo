"""Models module."""

from typing import Any, Optional


class BaseModel:
    """Base model class."""

    def __init__(self, name: str, value: Optional[Any] = None) -> None:
        """Initialize the model.
        
        Args:
            name: The name of the model
            value: Optional value to store
        """
        self.name = name
        self.value = value

    def __repr__(self) -> str:
        """String representation."""
        return f"BaseModel(name={self.name!r}, value={self.value!r})"

    def validate(self) -> bool:
        """Validate the model.
        
        Returns:
            True if valid, False otherwise
        """
        return bool(self.name)
