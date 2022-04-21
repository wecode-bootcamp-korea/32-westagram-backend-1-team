import json, re, bcrypt, jwt

from django.http  import JsonResponse
from django.views import View
from django.conf  import settings

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
            if User.objects.filter(email=email).exists():
                return JsonResponse({'message':'email_already_exists'}, status=400)

            User.objects.create(
                username    = username,
                email       = email,
                password    = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8'),
                phonenumber = phonenumber,
            )
            return JsonResponse({'message':'SUCCESS'},status=201)
        except KeyError:
            return JsonResponse({'message':'Key Error'},status=400)

class SingInView(View):
    def post(self, request):
        try:
            data     = json.loads(request.body)
            user     = User.objects.get(email=data['email'])

            if not bcrypt.checkpw(data['password'].encode('utf-8'), user.password.encode('utf-8')):
                return JsonResponse({'message':'INVALID_USER'},status=401)

            access_token = jwt.encode({'id': user.id}, settings.SECRET_KEY, algorithm = settings.ALGORITHM)

            return JsonResponse({'access_token' : access_token,},status=200)

        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)
        except ValueError:
            return JsonResponse({'message':'VALUE_ERROR'}, status=400)
        except User.DoesNotExist:
            return JsonResponse({'message' : 'INVALID_USER'}, status=401)