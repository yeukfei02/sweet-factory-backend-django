import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from zones.models import Zone


@csrf_exempt
@require_http_methods(["POST"])
def create_zone(request):
    print(f"request = {request}")

    response = {
        "message": "create_zone",
        "zone": {}
    }

    try:
        body = request.body

        body_json = json.loads(body)

        if body_json:
            zone_name = body_json.get("zone_name")
            user_id = body_json.get("user_id")

            zone = Zone.objects.create(
                zone_name=zone_name,
                user_id=user_id,
            )
            if zone:
                formatted_user = {
                    "id": zone.user.id,
                    "email": zone.user.email,
                    "created_at": zone.user.created_at,
                    "updated_at": zone.user.updated_at
                }

                formatted_zone = {
                    "id": zone.id,
                    "zone_name": zone.zone_name,
                    "user": formatted_user,
                    "created_at": zone.created_at,
                    "updated_at": zone.updated_at
                }

                response = {
                    "message": "create_zone",
                    "zone": formatted_zone
                }

                return JsonResponse(response, status=200)
    except Exception as e:
        response = {
            "message": "create_zone",
            "zone": {},
            "error": str(e)
        }
        return JsonResponse(response, status=400)


@csrf_exempt
@require_http_methods(["GET"])
def get_zones(request):
    print(f"request = {request}")

    user_id = request.GET.get('user_id')
    print(f"user_id = {user_id}")

    response = {
        "message": "getZones",
        "zones": []
    }

    try:
        zones = Zone.objects.all()

        if user_id:
            zones = Zone.objects.all().filter(user_id=user_id)

        formatted_zones = []

        if zones:
            for zone in zones:
                formatted_user = {
                    "id": zone.user.id,
                    "email": zone.user.email,
                    "created_at": zone.user.created_at,
                    "updated_at": zone.user.updated_at
                }

                formatted_zone = {
                    "id": zone.id,
                    "zone_name": zone.zone_name,
                    "user": formatted_user,
                    "created_at": zone.created_at,
                    "updated_at": zone.updated_at
                }
                formatted_zones.append(formatted_zone)

            response = {
                "message": "getZones",
                "getZones": formatted_zones
            }
            return JsonResponse(response, status=200)
        else:
            response = {
                "message": "getZones",
                "getZones": []
            }
            return JsonResponse(response, status=200)
    except Exception as e:
        response = {
            "message": "getZones",
            "getZones": [],
            "error": str(e)
        }
        return JsonResponse(response, status=400)


@csrf_exempt
@require_http_methods(["GET"])
def get_zone(request, id):
    print(f"request = {request}")
    print(f"id = {id}")

    response = {
        "message": "getZone",
        "zone": {}
    }

    try:
        zone = Zone.objects.get(id=id)
        if zone:
            formatted_user = {
                "id": zone.user.id,
                "email": zone.user.email,
                "created_at": zone.user.created_at,
                "updated_at": zone.user.updated_at
            }

            formatted_zone = {
                "id": zone.id,
                "zone_name": zone.zone_name,
                "user": formatted_user,
                "created_at": zone.created_at,
                "updated_at": zone.updated_at
            }

            response = {
                "message": "getZone",
                "zone": formatted_zone
            }
            return JsonResponse(response, status=200)
    except Exception as e:
        response = {
            "message": "getZone",
            "zone": {},
            "error": str(e)
        }
        return JsonResponse(response, status=400)
