import json, re
from django.http import JsonResponse
from django.views import View
from users.models import User


class SignUpView(View):
    def post(self, request):
        try:
            data           = json.loads(request.body)

            if re.match(r"^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", data["email"]) == None:
                return JsonResponse({'message': 'INVALID_EMAIL'}, status=400)

            if re.match(r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$", data["password"]) == None:
                return JsonResponse({'message': 'INVALID_PASSWORD'}, status=400)


            User.objects.create(
                username   = data['username'],
                first_name = data['first_name'],
                last_name  = data['last_name'],
                email      = data['email'],
                password   = data['password'],
                number     = data['number'],
            )
            return JsonResponse({'message':'created'}, status = 201)


        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)