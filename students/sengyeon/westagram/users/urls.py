from threading import local
from django.urls import path

from .views      import SignUpView

urlpatterns = [
    path('/signup', SignUpView.as_view()),
   path('/login', LogInView.as_view())
]