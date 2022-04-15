import json
from nis import match

from django.http import JsonResponse
from django.views import View

from users.models import User

class SignUpView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
                # email_regex  = '^([a-z0-9_\.-]+)@([\da-z\.-]+)\.([a-z\.]{2,6})$'
                # passwd_regex = '^(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9]).{8,}$'
            if User.objects.filter(email=data['email']).exists():
                return JsonResponse({'message':'email_already_exists'}, status=400)
            # if not re.match(email_regex, data['email']):
            #     return JsonResponse({'message':'invalid_email'}, status=400)
            # if not re.match(passwd_regex, data['email']):
            #     return JsonResponse({'message':'invalid_password'}, status=400)
            User.objects.create(username    = data['username'],
                                email       = data['email'],
                                password    = data['password'],
                                phonenumber = data['phonenumber']
                                )
            return JsonResponse({'message':'SUCCESS'},status=201)
        except ValueError:
            return JsonResponse({'message':'Key Error'},status=400)