from django.urls import path

from users.views import SignUpView

urlpatterns = [
    path('', SignUpView.as_view()),
    path('/signup', SignUpView.as_view()),
]
