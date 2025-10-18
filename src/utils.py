"""Utility functions for testing."""


def get_items() -> list:
    """Get list of items."""
    return [1, 2, 3]  # Intentionally returns 3 items for assertion error tests


def format_date(timestamp: int) -> str:
    """Format timestamp to date string."""
    # This will cause import error when datetime is not imported
    return datetime.fromtimestamp(timestamp).strftime("%Y-%m-%d")


def process_data(data: list) -> int:
    """Process data and return count."""
    return len(data)


def calculate_sum(numbers: list) -> int:
    """Calculate sum of numbers."""
    return sum(numbers)

