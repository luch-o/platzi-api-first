"""Module for application exceptions."""


class ApplicationError(Exception):
    """Base class for all application errors"""


class UserNotFoundError(ApplicationError):
    """Raised when a user is not found"""


class ProductNotFoundError(ApplicationError):
    """Raised when a product is not found"""
