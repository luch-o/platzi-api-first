"""Module for services classes with business logic."""

from src.models import User, Product
from src.exceptions import UserNotFoundError, ProductNotFoundError
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


class ProductService:
    def __init__(self, product_repository: RepositoryInterface[Product]):
        self.product_repository = product_repository

    def get_all_products(self) -> list[Product]:
        return self.product_repository.get_all()

    def create_product(self, product: Product) -> Product:
        return self.product_repository.create(product)

    def get_product(self, id: int) -> Product:
        product = self.product_repository.get_by_id(id)
        if not product:
            raise ProductNotFoundError("Product not found")
        return product

    def update_product(self, id: int, product: Product) -> Product:
        existing_product = self.get_product(id)
        product.id = existing_product.id
        return self.product_repository.update(product)

    def delete_product(self, id: int) -> None:
        existing_product = self.get_product(id)
        self.product_repository.delete(existing_product.id)