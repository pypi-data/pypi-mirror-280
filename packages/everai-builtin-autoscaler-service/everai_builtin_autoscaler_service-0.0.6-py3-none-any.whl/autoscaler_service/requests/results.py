import typing

from everai_autoscaler.model import DecideResult, Decorator, Factors
from pydantic import Field, BaseModel
from typing import Dict, List, Optional, Union


class DecorateRecord(BaseModel):
    source: Union[Dict[str, str], BaseModel]
    decorator: Decorator
    target: Union[Dict[str, str], BaseModel]


class Results(DecideResult):
    arguments: Optional[Dict[str, str]] = Field(default=None)
    factors: Optional[Factors] = Field(default=None)

    decorated_histories: Optional[List[DecorateRecord]] = Field(default=None)
