
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

            email_regex    = '[a-zA-Z0-9.-_+]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9.]+'
            password_regex = '^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$'

            if not re.match(email_regex, data['email']):
                return JsonResponse({'message' : 'INVALID_EMAIL'}, status = 400)
            if not re.match(password_regex, data['password']):
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
        
    
