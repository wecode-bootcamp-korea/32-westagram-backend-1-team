from django.urls import path
from users.views import SignUpView, SingInView

urlpatterns = [
    path('/signup', SignUpView.as_view()),
    path('/signin', SingInView.as_view()),
]
