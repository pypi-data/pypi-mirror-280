from __future__ import annotations
from pydantic import BaseModel, Field
from typing import Dict, List, Optional, Union, Callable


class Decorator(BaseModel):
    name: str
    arguments: Optional[Dict[str, Union[str, Callable[[], str]]]] = Field(default=None)

    @staticmethod
    def from_json(data) -> Decorator:
        return Decorator.model_validate_json(data)


class Decorators(BaseModel):
    arguments: Optional[List[Decorator]] = Field(default=None)
    factors: Optional[List[Decorator]] = Field(default=None)

    @staticmethod
    def from_json(data) -> Decorators:
        return Decorators.model_validate_json(data)
