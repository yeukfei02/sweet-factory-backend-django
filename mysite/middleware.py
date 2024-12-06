import jwt
import os


class AuthorizationMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        try:
            print(f"request.path = {request.path}")

            if request.path.startswith("/api/zones") or request.path.startswith("/api/cities"):
                authorization = request.headers.get("Authorization")
                if authorization:
                    token = authorization[7:]
                    print(f"token = {token}")

                    if token:
                        jwt_secret = os.getenv("JWT_SECRET")

                        decoded = jwt.decode(
                            token, jwt_secret, algorithms="HS256")
                        print(f"decoded = {decoded}")

                        decoded_email = decoded["email"]

                        if decoded and decoded_email:
                            response = self.get_response(request)
                            return response
            else:
                response = self.get_response(request)
                return response
        except Exception as e:
            print(f"AuthorizationMiddleware error = {e}")
