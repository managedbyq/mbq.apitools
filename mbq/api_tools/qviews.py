from typing import TypeVar, cast, Type
from django.http import HttpRequest, JsonResponse
from importlib import import_module

T = TypeVar('T')


from dataclasses import dataclass


@dataclass(frozen=True)
class QSchema:
    pass


def _construct_payload(payload: dict, schema_class: Type[QSchema]) -> QSchema:
    return schema_class(**payload)


def qview(func: T) -> T:
    def wrapper(request, *args, **kwargs):
        schema_class = func.__annotations__["payload"]
        print('schema_class', schema_class)
        the_payload = _construct_payload(request, schema_class)
        return func(request, the_payload, *args, **kwargs)

    return cast(T, wrapper)


@dataclass(frozen=True)
class TestSchema(QSchema):
    a: int
    b: str

@qview
def test_func(request: dict, payload: TestSchema, order_id: int) -> str:
    print("in test_func payload", request, payload)
    return 'abc'


test_func(request={'a': 1, 'b': 'b'}, order_id=1)