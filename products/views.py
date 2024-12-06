import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_http_methods
from products.models import Product


@csrf_exempt
@require_http_methods(["POST"])
def create_product(request):
    print(f"request = {request}")

    response = {
        "message": "create_product",
        "product": {}
    }

    try:
        body = request.body

        body_json = json.loads(body)

        if body_json:
            product_name = body_json.get("product_name")
            product_description = body_json.get("product_description")
            price = body_json.get("price")
            quantity = body_json.get("quantity")
            user_id = body_json.get("user_id")
            city_id = body_json.get("city_id")
            machine_id = body_json.get("machine_id")

            product = Product.objects.create(
                product_name=product_name,
                product_description=product_description,
                price=price,
                quantity=quantity,
                user_id=user_id,
                city_id=city_id,
                machine_id=machine_id
            )
            if product:
                formatted_user = {
                    "id": product.user.id,
                    "email": product.user.email,
                    "created_at": product.user.created_at,
                    "updated_at": product.user.updated_at
                }

                formatted_city = {
                    "id": product.city.id,
                    "area": product.city.area,
                    "city_name": product.city.city_name,
                    "created_at": product.city.created_at,
                    "updated_at": product.city.updated_at
                }

                formatted_machine = {
                    "id": product.machine.id,
                    "machine_name": product.machine.machine_name,
                    "serial_number": product.machine.serial_number,
                    "created_at": product.machine.created_at,
                    "updated_at": product.machine.updated_at
                }

                formatted_product = {
                    "id": product.id,
                    "product_name": product.product_name,
                    "user": formatted_user,
                    "city": formatted_city,
                    "machine": formatted_machine,
                    "created_at": product.created_at,
                    "updated_at": product.updated_at
                }

                response = {
                    "message": "create_product",
                    "product": formatted_product
                }

                return JsonResponse(response, status=200)
    except Exception as e:
        response = {
            "message": "create_product",
            "product": {},
            "error": str(e)
        }
        return JsonResponse(response, status=400)


@csrf_exempt
@require_http_methods(["GET"])
def get_products(request):
    print(f"request = {request}")

    user_id = request.GET.get('user_id')
    print(f"user_id = {user_id}")

    response = {
        "message": "getProducts",
        "products": []
    }

    try:
        products = Product.objects.all()

        if user_id:
            products = Product.objects.all().filter(user_id=user_id)

        formatted_products = []

        if products:
            for product in products:
                formatted_user = {
                    "id": product.user.id,
                    "email": product.user.email,
                    "created_at": product.user.created_at,
                    "updated_at": product.user.updated_at
                }

                formatted_city = {
                    "id": product.city.id,
                    "area": product.city.area,
                    "city_name": product.city.city_name,
                    "created_at": product.city.created_at,
                    "updated_at": product.city.updated_at
                }

                formatted_machine = {
                    "id": product.machine.id,
                    "machine_name": product.machine.machine_name,
                    "serial_number": product.machine.serial_number,
                    "created_at": product.machine.created_at,
                    "updated_at": product.machine.updated_at
                }

                formatted_product = {
                    "id": product.id,
                    "product_name": product.product_name,
                    "user": formatted_user,
                    "city": formatted_city,
                    "machine": formatted_machine,
                    "created_at": product.created_at,
                    "updated_at": product.updated_at
                }
                formatted_products.append(formatted_product)

            response = {
                "message": "getProducts",
                "getProducts": formatted_products
            }
            return JsonResponse(response, status=200)
        else:
            response = {
                "message": "getProducts",
                "getProducts": []
            }
            return JsonResponse(response, status=200)
    except Exception as e:
        response = {
            "message": "getProducts",
            "getProducts": [],
            "error": str(e)
        }
        return JsonResponse(response, status=400)


@csrf_exempt
@require_http_methods(["GET"])
def get_product(request, id):
    print(f"request = {request}")
    print(f"id = {id}")

    response = {
        "message": "getProduct",
        "product": {}
    }

    try:
        product = Product.objects.get(id=id)
        if product:
            formatted_user = {
                "id": product.user.id,
                "email": product.user.email,
                "created_at": product.user.created_at,
                "updated_at": product.user.updated_at
            }

            formatted_city = {
                "id": product.city.id,
                "area": product.city.area,
                "city_name": product.city.city_name,
                "created_at": product.city.created_at,
                "updated_at": product.city.updated_at
            }

            formatted_machine = {
                "id": product.machine.id,
                "machine_name": product.machine.machine_name,
                "serial_number": product.machine.serial_number,
                "created_at": product.machine.created_at,
                "updated_at": product.machine.updated_at
            }

            formatted_product = {
                "id": product.id,
                "product_name": product.product_name,
                "user": formatted_user,
                "city": formatted_city,
                "machine": formatted_machine,
                "created_at": product.created_at,
                "updated_at": product.updated_at
            }

            response = {
                "message": "getProduct",
                "product": formatted_product
            }
            return JsonResponse(response, status=200)
    except Exception as e:
        response = {
            "message": "getProduct",
            "product": {},
            "error": str(e)
        }
        return JsonResponse(response, status=400)
