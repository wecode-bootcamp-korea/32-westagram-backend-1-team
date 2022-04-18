import json, re # 파이썬 built-in package

from django.http import JsonResponse # third-party package
from django.views import View

from users.models import User   #직접 만든 package


class SignUpView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            
            username   = data['username']
            first_name = data['first_name']
            last_name  = data['last_name']
            email      = data['email']
            password   = data['password']
            number     = data['number']

            if not re.match(r"^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$", data["email"]):
                return JsonResponse({'message': 'INVALID_EMAIL'}, status=400) 

            if User.objects.filter(email = email).exists():
                return JsonResponse({'message' : 'Email_Already_Exists'}, status=400)

            if not re.match(r"^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$", data["password"]):
                return JsonResponse({'message': 'INVALID_PASSWORD'}, status=400)

            User.objects.create(
                username   = username,
                first_name = first_name,
                last_name  = last_name,
                email      = email,
                password   = password,
                number     = number,
            )
            return JsonResponse({'message':'created'}, status = 201)
        except KeyError:
            return JsonResponse({'message' : 'KEY_ERROR'}, status = 400)
