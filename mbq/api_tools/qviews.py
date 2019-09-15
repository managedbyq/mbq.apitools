from typing import TypeVar, cast
from django.http import HttpRequest, JsonResponse

T = TypeVar('T')


def qview(func: T) -> T:
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)

    return cast(T, wrapper())



@qview
def test_func(request: HttpRequest, order_id: int) -> JsonResponse:
    return JsonResponse('abc')


reveal_type(test_func)