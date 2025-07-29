"""Module for repositories on the infrastructure layer."""

from abc import ABC, abstractmethod
from typing import TypeVar, Generic

from src.models import User

T = TypeVar("T")


class RepositoryInterface(ABC, Generic[T]):
    @abstractmethod
    def get_all(self) -> list[T]:
        pass

    @abstractmethod
    def get_by_id(self, id: int) -> T:
        pass

    @abstractmethod
    def create(self, object: T) -> T:
        pass

    @abstractmethod
    def update(self, object: T) -> T:
        pass

    @abstractmethod
    def delete(self, id: int) -> None:
        pass


class UserMemoryRepository(RepositoryInterface[User]):
    def __init__(self):
        self.repository: list[User] = []

    def get_all(self) -> list[User]:
        return self.repository

    def get_by_id(self, id: int) -> User:
        for user in self.repository:
            if user.id == id:
                return user

    def create(self, object: User) -> User:
        object.id = len(self.repository) + 1
        self.repository.append(object)
        return object

    def update(self, object: User) -> User:
        self.repository[object.id - 1] = object
        return object

    def delete(self, id: int) -> None:
        self.repository.remove(self.get_by_id(id))
