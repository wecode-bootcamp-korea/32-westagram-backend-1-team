# from django.http import JsonResponse
# import re
# from users.models import User

# class Validate:
#     def email_validate(email):
#         regex_email    = '^[a-zA-Z0-9+-_.]+@[a-zA-Z0-9_-]+\.[a-zA-Z0-9-.]+$'
#         if not re.match(regex_email, 'email'):
#             return JsonResponse({'message' : 'INVALID_EMAIL'}, status=400)
        
#     def password_validate(password):
#         regex_password = '\S{8,}'
#         if not re.match(regex_password, 'password'):
#             return JsonResponse({'message' : 'INVALID_PASSWORD'}, status=400)