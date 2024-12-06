import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from machines.models import Machine


@csrf_exempt
@require_http_methods(["POST"])
def create_machine(request):
    print(f"request = {request}")

    response = {
        "message": "create_machine",
        "machine": {}
    }

    try:
        body = request.body

        body_json = json.loads(body)

        if body_json:
            machine_name = body_json.get("machine_name")
            serial_number = body_json.get("serial_number")
            user_id = body_json.get("user_id")
            city_id = body_json.get("city_id")

            machine = Machine.objects.create(
                machine_name=machine_name,
                serial_number=serial_number,
                user_id=user_id,
                city_id=city_id
            )
            if machine:
                formatted_user = {
                    "id": machine.user.id,
                    "email": machine.user.email,
                    "created_at": machine.user.created_at,
                    "updated_at": machine.user.updated_at
                }

                formatted_city = {
                    "id": machine.city.id,
                    "area": machine.city.area,
                    "city_name": machine.city.city_name,
                    "created_at": machine.city.created_at,
                    "updated_at": machine.city.updated_at
                }

                formatted_machine = {
                    "id": machine.id,
                    "machine_name": machine.machine_name,
                    "serial_number": serial_number,
                    "user": formatted_user,
                    "city": formatted_city,
                    "created_at": machine.created_at,
                    "updated_at": machine.updated_at
                }

                response = {
                    "message": "create_machine",
                    "machine": formatted_machine
                }

                return JsonResponse(response, status=200)
    except Exception as e:
        response = {
            "message": "create_machine",
            "machine": {},
            "error": str(e)
        }
        return JsonResponse(response, status=400)


@csrf_exempt
@require_http_methods(["GET"])
def get_machines(request):
    print(f"request = {request}")

    user_id = request.GET.get('user_id')
    print(f"user_id = {user_id}")

    response = {
        "message": "getMachines",
        "machines": []
    }

    try:
        machines = Machine.objects.all()

        if user_id:
            machines = Machine.objects.all().filter(user_id=user_id)

        formatted_machines = []

        if machines:
            for machine in machines:
                formatted_user = {
                    "id": machine.user.id,
                    "email": machine.user.email,
                    "created_at": machine.user.created_at,
                    "updated_at": machine.user.updated_at
                }

                formatted_city = {
                    "id": machine.city.id,
                    "area": machine.city.area,
                    "city_name": machine.city.city_name,
                    "created_at": machine.city.created_at,
                    "updated_at": machine.city.updated_at
                }

                formatted_machine = {
                    "id": machine.id,
                    "machine_name": machine.machine_name,
                    "serial_number": machine.serial_number,
                    "user": formatted_user,
                    "city": formatted_city,
                    "created_at": machine.created_at,
                    "updated_at": machine.updated_at
                }
                formatted_machines.append(formatted_machine)

            response = {
                "message": "getMachines",
                "getMachines": formatted_machines
            }
            return JsonResponse(response, status=200)
        else:
            response = {
                "message": "getMachines",
                "getMachines": []
            }
            return JsonResponse(response, status=200)
    except Exception as e:
        response = {
            "message": "getMachines",
            "getMachines": [],
            "error": str(e)
        }
        return JsonResponse(response, status=400)


@csrf_exempt
@require_http_methods(["GET"])
def get_machine(request, id):
    print(f"request = {request}")
    print(f"id = {id}")

    response = {
        "message": "getMachine",
        "machine": {}
    }

    try:
        machine = Machine.objects.get(id=id)
        if machine:
            formatted_user = {
                "id": machine.user.id,
                "email": machine.user.email,
                "created_at": machine.user.created_at,
                "updated_at": machine.user.updated_at
            }

            formatted_city = {
                "id": machine.city.id,
                "area": machine.city.area,
                "city_name": machine.city.city_name,
                "created_at": machine.city.created_at,
                "updated_at": machine.city.updated_at
            }

            formatted_machine = {
                "id": machine.id,
                "machine_name": machine.machine_name,
                "serial_number": machine.serial_number,
                "user": formatted_user,
                "city": formatted_city,
                "created_at": machine.created_at,
                "updated_at": machine.updated_at
            }

            response = {
                "message": "getMachine",
                "machine": formatted_machine
            }
            return JsonResponse(response, status=200)
    except Exception as e:
        response = {
            "message": "getMachine",
            "machine": {},
            "error": str(e)
        }
        return JsonResponse(response, status=400)
