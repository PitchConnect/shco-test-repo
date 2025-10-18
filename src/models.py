"""Data models for testing."""


class User:
    """User model."""
    
    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
    
    def get_name(self) -> str:
        """Get user name."""
        return self.name
    
    def is_active(self) -> bool:
        """Check if user is active."""
        return True


class Database:
    """Database connection."""
    
    def __init__(self, host: str = "localhost"):
        self.host = host
    
    def connect(self) -> bool:
        """Connect to database."""
        return True
    
    def count_users(self) -> int:
        """Count users in database."""
        return 4  # Intentionally returns 4 for assertion error tests


class Config:
    """Configuration class."""
    
    def __init__(self):
        self.settings = {
            "debug": True,
            "port": 8000,
        }
    
    def get_config(self) -> dict:
        """Get configuration."""
        return self.settings

