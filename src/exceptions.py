"""Module for application exceptions."""


class ApplicationError(Exception):
    """Base class for all application errors"""


class UserNotFoundError(ApplicationError):
    """Raised when a user is not found"""
