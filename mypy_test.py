from django.http import HttpRequest, JsonResponse
from mbq.api_tools.qviews import qview


@qview()
def f(request:HttpRequest, order_id: int) -> JsonResponse:
    return JsonResponse('abc')