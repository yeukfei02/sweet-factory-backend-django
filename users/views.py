from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from django.forms.models import model_to_dict
import json
from users.models import User


@csrf_exempt
@require_http_methods(["POST"])
def create_user(request):
    print(f"request = {request}")

    response = {
        "message": "createUser",
        "user": {}
    }

    try:
        body = request.body

        body_json = json.loads(body)

        if body_json:
            email = body_json.get("email")
            password = body_json.get("password")

            user = User.objects.create(
                email=email,
                password=password,
            )

            response = {
                "message": "createUser",
                "user": model_to_dict(user)
            }

            return JsonResponse(response, status=200)
    except Exception as e:
        response = {
            "message": "createUser",
            "user": {},
            "error": str(e)
        }
        return JsonResponse(response, status=400)


@csrf_exempt
@require_http_methods(["GET"])
def get_users(request):
    print(f"request = {request}")

    response = {
        "message": "getUsers",
        "users": []
    }

    try:
        users = User.objects.all().values()

        response = {
            "message": "getUsers",
            "users": list(users)
        }
        return JsonResponse(response, status=200)
    except Exception as e:
        response = {
            "message": "getUsers",
            "users": [],
            "error": str(e)
        }
        return JsonResponse(response, status=400)


@csrf_exempt
@require_http_methods(["GET"])
def get_user(request, id):
    print(f"request = {request}")
    print(f"id = {id}")

    response = {
        "message": "getUser",
        "user": {}
    }

    try:
        user = User.objects.get(id=id)

        response = {
            "message": "getUser",
            "user": model_to_dict(user)
        }
        return JsonResponse(response, status=200)
    except Exception as e:
        response = {
            "message": "getUser",
            "user": {},
            "error": str(e)
        }
        return JsonResponse(response, status=400)
