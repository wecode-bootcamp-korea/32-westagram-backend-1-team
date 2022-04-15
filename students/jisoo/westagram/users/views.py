
import json

from django.http import JsonResponse
from django.views import View

from users.models import User

class SignupView(View):
    def post(self, request):
        try:
            data = json.loads(request.body)
            User.objects.create(
                username     = ['username'],
                first_name   = ['first_name'],
                last_name    = ['last_name'],
                email        = ['email'],
                password     = ['password'],
                phone_number = ['phone_number'],
            )
            return JsonResponse({'message':'SUCCESS'}, status=201)
        except KeyError:
            return JsonResponse({'message':'KEY_ERROR'}, status=400)
        
    
