
# def f(request:, a2: str) -> str:
#     return 'abc'
#
# reveal_type(f)

from django.http import HttpRequest, JsonResponse
from mbq.api_tools.views import View, view
from mbq.api_tools import fields
from decimal import Decimal
@view(params={
    'a': fields.String()
})
def g(request:HttpRequest, vendor_id: str) -> JsonResponse:
    params = request.params
    payload = request.payload
    return JsonResponse('abc')


reveal_type(g)

#
# from typing import TypeVar, cast, Callable
#
# T = TypeVar('T')
# def dec(func: T) -> T:
#     def ret(*args, **kwargs):
#         return func(*args, **kwargs)
#
#     return cast(T, ret)
#
# @dec
# def h(a1: int, a2: str) -> str:
#     return 'abc'
#
# reveal_type(h)
#
#
# G = TypeVar('G', bound=Callable)
# from functools import wraps
# def decwraps(func: G) -> G:
#     @wraps(func)
#     def ret(*args, **kwargs):
#         return func(*args, **kwargs)
#
#     return cast(G, ret)
#
# @decwraps
# def i(a1: int, a2: str) -> str:
#     return 'abc'
#
# reveal_type(i)

#
# from django.http import HttpRequest, JsonResponse
# from functools import wraps
# from django.views.decorators.csrf import csrf_exempt
# from typing import Union
# from uuid import UUID
# # Arg = TypeVar('Arg', bound=Union[str, int, UUID])
# Arg = Union[str, int, UUID]
# J1 = Callable[[HttpRequest], JsonResponse]
# J2 = Callable[[HttpRequest, str], JsonResponse]
# J3 = Callable[[HttpRequest, int], JsonResponse]
# J4 = Callable[[HttpRequest, UUID], JsonResponse]
# J5 = Callable[[HttpRequest, str, str], JsonResponse]
# J6 = Callable[[HttpRequest, int, int], JsonResponse]
# J7 = Callable[[HttpRequest, UUID, UUID], JsonResponse]
# J8 = Callable[[HttpRequest, str, int], JsonResponse]
# J9 = Callable[[HttpRequest, int, str], JsonResponse]
# J10 = Callable[[HttpRequest, str, UUID], JsonResponse]
# J11 = Callable[[HttpRequest, UUID, str], JsonResponse]
# J12 = Callable[[HttpRequest, int, UUID], JsonResponse]
# J13 = Callable[[HttpRequest, UUID, int], JsonResponse]
# J = TypeVar('J', bound=Union[J1, J2, J3, J4, J5, J6, J7, J8, J9, J10, J11, J12, J13])
# def jwraps(func: J) -> J:
#     @wraps(func)
#     def ret(*args, **kwargs):
#         return func(*args, **kwargs)
#
#     return cast(J, csrf_exempt(ret))
#
# @jwraps
# def j1(request: HttpRequest) -> JsonResponse:
#     return JsonResponse('blabla')
#
# reveal_type(j1)
#
# from decimal import Decimal
# @jwraps
# def j2(request: HttpRequest, order_id: int, person_id: UUID) -> JsonResponse:
#     return JsonResponse('blabla')
#
# reveal_type(j2)


# from django.http import HttpRequest, JsonResponse
# from functools import wraps
# from typing import Protocol
#
# class K(Protocol):
#     def __call__(self, request: HttpRequest, *args: str) -> JsonResponse: ...
#
# def kwraps(func: K) -> K:
#     @wraps(func)
#     def ret(*args, **kwargs):
#         return func(*args, **kwargs)
#
#     return cast(K, ret)
#
# @kwraps
# def k(request: HttpRequest, a: str, b: str) -> JsonResponse:
#     return JsonResponse('blabla')
#
# reveal_type(k)
