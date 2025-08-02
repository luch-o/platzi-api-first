"""Module for the main application."""

from fastapi import FastAPI, Request, status, HTTPException
from fastapi.responses import JSONResponse
import yaml
from pathlib import Path
from src.schemas import HelloResponse, UserPayload, UserResponse, ProductPayload, ProductResponse
from src.models import User, Product
from src.services import UserService, ProductService
from pydantic import ValidationError
from src.repositories import UserMemoryRepository, ProductMemoryRepository
from src.exceptions import UserNotFoundError, ProductNotFoundError

app = FastAPI()


# Read and load the OpenAPI schema from openapi.yaml
def load_openapi_schema():
    openapi_path = Path(__file__).parent.parent / "docs" / "openapi.yaml"
    with open(openapi_path, "r") as f:
        return yaml.safe_load(f)


app.openapi_schema = load_openapi_schema()


@app.exception_handler(ValidationError)
async def validation_error_handler(request: Request, exc: ValidationError):
    return JSONResponse(
        status_code=status.HTTP_400_BAD_REQUEST,
        content={
            "message": ", ".join(error.msg for error in exc.errors()),
        },
    )


user_service = UserService(UserMemoryRepository())
product_service = ProductService(ProductMemoryRepository())


@app.get("/hello")
def hello() -> HelloResponse:
    return {"message": "Hello World"}


@app.post("/users")
def create_user(user: UserPayload) -> UserResponse:
    user = User.model_validate(user.model_dump())
    return user_service.create_user(user)


@app.get("/users/{id}")
def get_user(id: int) -> UserResponse:
    try:
        return user_service.get_user(id)
    except UserNotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e)) from e


@app.patch("/users/{id}")
def update_user(id: int, user: UserPayload) -> UserResponse:
    try:
        user = User.model_validate(user.model_dump())
        return user_service.update_user(id, user)
    except UserNotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e)) from e


@app.get("/products")
def get_all_products() -> list[ProductResponse]:
    return product_service.get_all_products()


@app.post("/products")
def create_product(product: ProductPayload) -> ProductResponse:
    product = Product.model_validate(product.model_dump())
    return product_service.create_product(product)


@app.get("/products/{id}")
def get_product(id: int) -> ProductResponse:
    try:
        return product_service.get_product(id)
    except ProductNotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e)) from e


@app.patch("/products/{id}")
def update_product(id: int, product: ProductPayload) -> ProductResponse:
    try:
        product = Product.model_validate(product.model_dump())
        return product_service.update_product(id, product)
    except ProductNotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e)) from e


@app.delete("/products/{id}")
def delete_product(id: int):
    try:
        product_service.delete_product(id)
        return JSONResponse(status_code=status.HTTP_204_NO_CONTENT, content=None)
    except ProductNotFoundError as e:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=str(e)) from e
