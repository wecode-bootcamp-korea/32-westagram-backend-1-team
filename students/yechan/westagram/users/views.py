import json, re

from django.http  import JsonResponse, HttpResponse
from django.views import View

from users.models import User

class SignUpView(View):
    def post(self, request):
        try:
            data           = json.loads(request.body)
            email          = data['email']
            password       = data['password']
            username       = data['username']
            phonenumber    = data['phonenumber']
            regex_email    = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9_-]+\.[a-zA-Z0-9-.]+$'
            regex_password = "^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$"

            if not re.match(regex_email, email):
                return JsonResponse({'message' : 'INVALID_EMAIL'}, status=400)
            if not re.match(regex_password, password):
                return JsonResponse({'message' : 'INVALID_PASSWORD'}, status=400)
            if User.objects.filter(email=data['email']).exists():
                return JsonResponse({'message':'email_already_exists'}, status=400)

            User.objects.create(
                username    = username,
                email       = email,
                password    = password,
                phonenumber = phonenumber,
            )
            return JsonResponse({'message':'SUCCESS'},status=201)
        except KeyError:
            return JsonResponse({'message':'Key Error'},status=400)