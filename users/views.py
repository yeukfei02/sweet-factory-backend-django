import os
import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
import bcrypt
import jwt
from datetime import datetime, timedelta
from users.models import User


@csrf_exempt
@require_http_methods(["POST"])
def signup(request):
    print(f"request = {request}")

    response = {
        "message": "signup",
        "user": {}
    }

    try:
        body = request.body

        body_json = json.loads(body)

        if body_json:
            email = body_json.get("email")
            password = body_json.get("password")

            salt = bcrypt.gensalt()

            hashed_password = bcrypt.hashpw(
                password=password,
                salt=salt
            )

            user = User.objects.create(
                email=email,
                password=hashed_password,
            )
            if user:
                formatted_user = {
                    "id": user.id,
                    "email": user.email,
                    "created_at": user.created_at,
                    "updated_at": user.updated_at
                }

                response = {
                    "message": "signup",
                    "user": formatted_user
                }

                return JsonResponse(response, status=200)
    except Exception as e:
        response = {
            "message": "signup",
            "user": {},
            "error": str(e)
        }
        return JsonResponse(response, status=400)


@csrf_exempt
@require_http_methods(["POST"])
def login(request):
    print(f"request = {request}")

    response = {
        "message": "login",
        "user": {},
        "token": ""
    }

    try:
        body = request.body

        body_json = json.loads(body)

        if body_json:
            email = body_json.get("email")
            password = body_json.get("password")

            user = User.objects.get(email=email)
            if user:
                user_password = user.password

                is_valid_password = bcrypt.checkpw(
                    password=password,
                    hashed_password=user_password
                )
                print(f"is_valid_password = {is_valid_password}")

                if is_valid_password:
                    formatted_user = {
                        "id": user.id,
                        "email": user.email,
                        "created_at": user.created_at,
                        "updated_at": user.updated_at
                    }

                    jwt_secret = os.getenv("JWT_SECRET")

                    token = jwt.encode(
                        {
                            "email": email,
                            "exp": datetime.now() + timedelta(days=1)
                        },
                        jwt_secret,
                        algorithm="HS256",
                    )

                    response = {
                        "message": "login",
                        "user": formatted_user,
                        "token": token
                    }

                    return JsonResponse(response, status=200)
                else:
                    response = {
                        "message": "login",
                        "user": {},
                        "token": "",
                        "error": "Invalid password"
                    }
                    return JsonResponse(response, status=400)
    except Exception as e:
        response = {
            "message": "login",
            "user": {},
            "token": "",
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
        users = User.objects.all()

        formatted_users = []

        if users:
            for user in users:
                formatted_user = {
                    "id": user.id,
                    "email": user.email,
                    "created_at": user.created_at,
                    "updated_at": user.updated_at
                }
                formatted_users.append(formatted_user)

            response = {
                "message": "getUsers",
                "users": formatted_users
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
        if user:
            formatted_user = {
                "id": user.id,
                "email": user.email,
                "created_at": user.created_at,
                "updated_at": user.updated_at
            }

            response = {
                "message": "getUser",
                "user": formatted_user
            }
            return JsonResponse(response, status=200)
    except Exception as e:
        response = {
            "message": "getUser",
            "user": {},
            "error": str(e)
        }
        return JsonResponse(response, status=400)
