"""Validators for testing."""

from src.models import UserProfile


class ProfileValidator:
    """Validator for user profiles."""
    
    def __init__(self, profile: UserProfile):
        self.profile = profile
    
    def is_valid(self) -> bool:
        """Check if profile is valid."""
        return self.profile.is_complete() and len(self.profile.get_bio()) > 0

