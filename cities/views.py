import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from cities.models import City


@csrf_exempt
@require_http_methods(["POST"])
def create_city(request):
    print(f"request = {request}")

    response = {
        "message": "create_city",
        "city": {}
    }

    try:
        body = request.body

        body_json = json.loads(body)

        if body_json:
            area = body_json.get("area")
            city_name = body_json.get("city_name")
            user_id = body_json.get("user_id")
            zone_id = body_json.get("zone_id")

            city = City.objects.create(
                area=area,
                city_name=city_name,
                user_id=user_id,
                zone_id=zone_id,
            )
            if city:
                formatted_user = {
                    "id": city.user.id,
                    "email": city.user.email,
                    "created_at": city.user.created_at,
                    "updated_at": city.user.updated_at
                }

                formatted_zone = {
                    "id": city.zone.id,
                    "zone_name": city.zone.zone_name,
                    "created_at": city.zone.created_at,
                    "updated_at": city.zone.updated_at
                }

                formatted_city = {
                    "id": city.id,
                    "area": city.area,
                    "city_name": city.city_name,
                    "user": formatted_user,
                    "zone": formatted_zone,
                    "created_at": city.created_at,
                    "updated_at": city.updated_at
                }

                response = {
                    "message": "create_city",
                    "city": formatted_city
                }

                return JsonResponse(response, status=200)
    except Exception as e:
        response = {
            "message": "create_city",
            "city": {},
            "error": str(e)
        }
        return JsonResponse(response, status=400)


@csrf_exempt
@require_http_methods(["GET"])
def get_cities(request):
    print(f"request = {request}")

    user_id = request.GET.get('user_id')
    print(f"user_id = {user_id}")

    response = {
        "message": "getCitys",
        "citys": []
    }

    try:
        cities = City.objects.all()

        if user_id:
            cities = City.objects.all().filter(user_id=user_id)

        formatted_cities = []

        if cities:
            for city in cities:
                formatted_user = {
                    "id": city.user.id,
                    "email": city.user.email,
                    "created_at": city.user.created_at,
                    "updated_at": city.user.updated_at
                }

                formatted_zone = {
                    "id": city.zone.id,
                    "zone_name": city.zone.zone_name,
                    "created_at": city.zone.created_at,
                    "updated_at": city.zone.updated_at
                }

                formatted_city = {
                    "id": city.id,
                    "area": city.area,
                    "city_name": city.city_name,
                    "user": formatted_user,
                    "zone": formatted_zone,
                    "created_at": city.created_at,
                    "updated_at": city.updated_at
                }
                formatted_cities.append(formatted_city)

            response = {
                "message": "getCities",
                "cities": formatted_cities
            }
            return JsonResponse(response, status=200)
        else:
            response = {
                "message": "getCities",
                "cities": []
            }
            return JsonResponse(response, status=200)
    except Exception as e:
        response = {
            "message": "getCities",
            "cities": [],
            "error": str(e)
        }
        return JsonResponse(response, status=400)


@csrf_exempt
@require_http_methods(["GET"])
def get_city(request, id):
    print(f"request = {request}")
    print(f"id = {id}")

    response = {
        "message": "getCity",
        "city": {}
    }

    try:
        city = City.objects.get(id=id)
        if city:
            formatted_user = {
                "id": city.user.id,
                "email": city.user.email,
                "created_at": city.user.created_at,
                "updated_at": city.user.updated_at
            }

            formatted_zone = {
                "id": city.zone.id,
                "zone_name": city.zone.zone_name,
                "created_at": city.zone.created_at,
                "updated_at": city.zone.updated_at
            }

            formatted_city = {
                "id": city.id,
                "area": city.area,
                "city_name": city.city_name,
                "user": formatted_user,
                "zone": formatted_zone,
                "created_at": city.created_at,
                "updated_at": city.updated_at
            }

            response = {
                "message": "getCity",
                "city": formatted_city
            }
            return JsonResponse(response, status=200)
    except Exception as e:
        response = {
            "message": "getCity",
            "city": {},
            "error": str(e)
        }
        return JsonResponse(response, status=400)
