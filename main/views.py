from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods


@csrf_exempt
@require_http_methods(["GET"])
def get_main(request):
    print(f"request = {request}")

    response = {
        "message": "sweet-factory-backend-django",
    }
    return JsonResponse(response, status=200)
