from __future__ import annotations
from pydantic import BaseModel, Field
from typing import Dict, List


class Decorator(BaseModel):
    name: str
    arguments: Dict[str, str] = Field(default=None)

    @staticmethod
    def from_json(data) -> Decorator:
        return Decorator.model_validate_json(data)


class Decorators(BaseModel):
    arguments: List[Decorator] = Field(default=None)
    factors: List[Decorator] = Field(default=None)

    @staticmethod
    def from_json(data) -> Decorators:
        return Decorators.model_validate_json(data)
