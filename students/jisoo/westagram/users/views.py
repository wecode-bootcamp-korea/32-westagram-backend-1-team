
import json, re, bcrypt, jwt

from django.views     import View
from django.http      import JsonResponse
from django.db.models import Q
from my_settings      import SECRET_KEY, ALGORITHM

from users.models     import User  

class SignupView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            
            email            = data['email']
            hashed_password  = bcrypt.hashpw((data['password']).encode('utf-8'), bcrypt.gensalt())

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
                password     = hashed_password.decode('utf-8)'),
                phone_number = data['phone_number']
            )

            return JsonResponse({'message':'SUCCESS'}, status=201)
        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)
        
class LoginView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)

            user            = User.object.get(email=data['email'])
            hashed_password = user.password.encode('uft-8')
            access_token    = jwt.encode({'id': user.id}, SECRET_KEY, algorithm=ALGORITHM)

            if not bcrypt.checkpw(data['password'].encode('utf-8'), hashed_password):
                return JsonResponse({'message': "INVALID_USER"}, status=401)
            
            return JsonResponse({'message':'SUCCESS'}, access_token, status=200)
        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)
