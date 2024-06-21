import logging
from typing import TypeVar, Dict, Tuple, List, Callable
from pydantic import BaseModel

from autoscaler_service.requests import Requests, Results, DecorateRecord
from everai_autoscaler.builtin.decorator.arguments import ArgumentsFactory
from everai_autoscaler.builtin.decorator.factors import FactorsFactory
from everai_autoscaler.model import Decorator

T = TypeVar('T', Dict[str, str], BaseModel)


def _apply(source: T, decorators: List[Decorator]) -> Tuple[T, List[DecorateRecord]]:
    records = []
    for decorator in decorators or []:
        try:
            factor_decorator = FactorsFactory().create(decorator.name, decorator.arguments)
        except ValueError as e:
            logging.warning(f'factor decorator {decorator.name} not found, ignore it {e}')
            continue

        target = factor_decorator(source)
        DecorateRecord(source=source, decorator=decorator, target=target)
        records.append(DecorateRecord(source=source, decorator=decorator, target=target))
        source = target
    return source, records


def apply_decorators(req: Requests) -> Results:
    _factors, _factors_records = _apply(
        req.factors,
        req.decorators.factors if req.decorators and req.decorators.factors else [])
    _arguments, _arguments_records = _apply(
        req.arguments,
        req.decorators.arguments if req.decorators and req.decorators.arguments else [])

    histories = _factors_records.extend(_arguments_records)

    result = Results(
        arguements=_arguments,
        factors=_factors,
        decorated_histories=histories,
        # place holder
        max_workers=0,
        actions=[]
    )
    return result
