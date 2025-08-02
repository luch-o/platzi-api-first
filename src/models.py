"""Module for domain models."""

from typing import Optional, Literal, Dict, Any
from pydantic import BaseModel, Field, EmailStr


class User(BaseModel):
    id: Optional[int] = None
    name: str = Field(..., min_length=2)
    email: EmailStr
    age: int = Field(..., ge=18)


class Rating(BaseModel):
    score: float = Field(..., ge=0, le=5)
    comment: str = Field(..., min_length=10, max_length=200)


class Product(BaseModel):
    id: Optional[int] = None
    name: str
    price: float
    category: Literal["Electronics", "Clothing", "Books", "Food", "Other"]
    description: Optional[str] = None
    tags: Optional[list[str]] = Field(None, min_length=1)
    stock: Optional[bool] = None
    additional_properties: Optional[Dict[str, Any]] = None
    ratings: Optional[list[Rating]] = None
