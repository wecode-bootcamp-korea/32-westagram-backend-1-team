import json

from django.http import JsonResponse
from django.views import View

from signup.models import Users

class Singup(View):
    def post(self, request):
        