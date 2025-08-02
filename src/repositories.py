"""Module for repositories on the infrastructure layer."""

from abc import ABC, abstractmethod
from typing import TypeVar, Generic

from src.models import User, Product

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


class ProductMemoryRepository(RepositoryInterface[Product]):
    def __init__(self):
        self.repository: list[Product] = []

    def get_all(self) -> list[Product]:
        return self.repository

    def get_by_id(self, id: int) -> Product:
        for product in self.repository:
            if product.id == id:
                return product

    def create(self, object: Product) -> Product:
        object.id = len(self.repository) + 1
        self.repository.append(object)
        return object

    def update(self, object: Product) -> Product:
        self.repository[object.id - 1] = object
        return object

    def delete(self, id: int) -> None:
        self.repository.remove(self.get_by_id(id))
