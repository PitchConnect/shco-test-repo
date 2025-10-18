"""Models module."""

from typing import Any, Optional


class Model:
    """Base model class."""

    def __init__(self, name: str, value: Optional[int] = None) -> None:
        """Initialize the model.
        
        Args:
            name: The model name
            value: Optional integer value
        """
        if not isinstance(name, str):
            raise TypeError(f"name must be a string, got {type(name).__name__}")
        if value is not None and not isinstance(value, int):
            raise TypeError(f"value must be an integer or None, got {type(value).__name__}")
        
        self.name = name
        self.value = value if value is not None else 0

    def process(self, data: Any) -> Any:
        """Process data.
        
        Args:
            data: Data to process
            
        Returns:
            Processed data
        """
        if data is None:
            raise ValueError("data cannot be None")
        return data

    def __repr__(self) -> str:
        """Return string representation."""
        return f"Model(name={self.name!r}, value={self.value})"

    def __eq__(self, other: object) -> bool:
        """Check equality."""
        if not isinstance(other, Model):
            return NotImplemented
        return self.name == other.name and self.value == other.value
