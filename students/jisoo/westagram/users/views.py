
import json, re

from django.views import View
from django.http  import JsonResponse

from users.models import User

class SignupView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            
            email    = data['email'],
            password = data['password'],

            EMAIL_REGEX    = '[a-zA-Z0-9.-_+]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9.]+'
            PASSWORD_REGEX = '^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$'

            if not re.match(EMAIL_REGEX, data['email']):
                return JsonResponse({'message' : 'INVALID_EMAIL'}, status = 400)
                
            if not re.match(PASSWORD_REGEX, data['password']):
                return JsonResponse({'message' : 'INVALID_PASSWORD'}, status = 400)
            
            if User.objects.filter(email = email).exists():
                return JsonResponse({'MESSAGE' :'ALREADY_EXISTS_EMAIL'}, status=400)
            
            User.objects.create(
                username     = data['username'],
                first_name   = data['first_name'],
                last_name    = data['last_name'],
                email        = data['email'],
                password     = data['password'],
                phone_number = data['phone_number'],
            )

            return JsonResponse({'message':'SUCCESS'}, status=201)
        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)
        
class LoginView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            email    = data['email'],
            password = data['password'],

            if User.objects.filter(email = email).exists():
                    return JsonResponse({'message':'INVALID_USER'}, status=401)

            if User.objects.filter(password = password).exists():
                return JsonResponse({'message':'INVALID_USER'}, status=401)

            return JsonResponse({'message':'SUCCESS'}, status=200)
        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)
