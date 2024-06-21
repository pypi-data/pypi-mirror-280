from __future__ import annotations
import typing

from everai_autoscaler.model import Factors, Decorators
from pydantic import BaseModel, field_validator, Field


class Requests(BaseModel):
    factors: Factors = Field(default={})

    name: str = Field(default="")

    arguments: typing.Dict[str, str] = Field(default={})

    decorators: typing.Optional[Decorators] = Field(default=None)

    @staticmethod
    def from_json(data) -> Requests:
        return Requests.model_validate_json(data)
