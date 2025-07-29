"""Module for infrastucture schemas."""

from pydantic import BaseModel, Field, EmailStr


class HelloResponse(BaseModel):
    message: str


class ErrorResponse(BaseModel):
    message: str


class UserPayload(BaseModel):
    name: str = Field(..., min_length=2)
    email: EmailStr
    age: int = Field(..., ge=18)


class UserResponse(UserPayload):
    id: int
