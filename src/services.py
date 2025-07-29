"""Module for services classes with business logic."""

from src.models import User
from src.exceptions import UserNotFoundError
from src.repositories import RepositoryInterface


class UserService:
    def __init__(self, user_repository: RepositoryInterface[User]):
        self.user_repository = user_repository

    def create_user(self, user: User):
        return self.user_repository.create(user)

    def get_user(self, id: int) -> User:
        user = self.user_repository.get_by_id(id)
        if not user:
            raise UserNotFoundError("User not found")
        return user

    def update_user(self, id: int, user: User) -> User:
        existing_user = self.get_user(id)
        user.id = existing_user.id
        return self.user_repository.update(user)

    def delete_user(self, id: int) -> None:
        self.user_repository.delete(id)
