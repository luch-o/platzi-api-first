"""Module for domain models."""

from typing import Optional
from pydantic import BaseModel, Field, EmailStr


class User(BaseModel):
    id: Optional[int] = None
    name: str = Field(..., min_length=2)
    email: EmailStr
    age: int = Field(..., ge=18)
