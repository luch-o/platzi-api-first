"""Module for the main application."""

from fastapi import FastAPI, Request, status, HTTPException
from fastapi.responses import JSONResponse
import yaml
from pathlib import Path
from src.schemas import HelloResponse, UserPayload, UserResponse
from src.models import User
from src.services import UserService
from pydantic import ValidationError
from src.repositories import UserMemoryRepository
from src.exceptions import UserNotFoundError

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
