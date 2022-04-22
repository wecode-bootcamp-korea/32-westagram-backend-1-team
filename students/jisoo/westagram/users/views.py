
import json, re, bcrypt, jwt

from django.views import View
from django.http  import JsonResponse
from django.conf  import settings 

from users.models import User  

class SignupView(View):
    def post(self, request):
        try:
            data  = json.loads(request.body)
            email = data['email']

            EMAIL_REGEX    = '[a-zA-Z0-9.-_+]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9.]+'
            PASSWORD_REGEX = '^(?=.*[A-Za-z])(?=.*\d)(?=.*[$@$!%*#?&])[A-Za-z\d$@$!%*#?&]{8,}$'

            if not re.match(EMAIL_REGEX, data['email']):
                return JsonResponse({'message' : 'INVALID_EMAIL'}, status = 400)
            
            if not re.match(PASSWORD_REGEX, data['password']):
                return JsonResponse({'message' : 'INVALID_PASSWORD'}, status = 400)
            
            if User.objects.filter(email = email).exists():
                return JsonResponse({'MESSAGE' :'ALREADY_EXISTS_EMAIL'}, status=400)
            
            hashed_password  = bcrypt.hashpw((data['password']).encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

            User.objects.create(
                username     = data['username'],
                first_name   = data['first_name'],
                last_name    = data['last_name'],
                email        = data['email'],
                password     = hashed_password,
                phone_number = data['phone_number']
            )

            return JsonResponse({'message':'SUCCESS'}, status=201)
        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)
        
class LoginView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            user            = User.objects.get(email=data['email'])
            hashed_password = user.password.encode('utf-8')
            access_token    = jwt.encode({'id': user.id}, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

            if not bcrypt.checkpw(data['password'].encode('utf-8'), hashed_password):
                return JsonResponse({'message': "INVALID_USER"}, status=401)
            
            return JsonResponse({'message':'SUCCESS', 'token': access_token}, status=200)

        except User.DoesNotExist:
            return JsonResponse({"MESSAGE": "INVALID_USER"}, status=404)

        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)
