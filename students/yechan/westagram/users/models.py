from django.db import models

class User(models.Model):
    username    = models.CharField(max_length=20)
    email       = models.EmailField(max_length=254, unique=True)
    password    = models.CharField(max_length=100)
    phonenumber = models.CharField(max_length=20)
    created_at  = models.DateField(auto_now_add=True)
    updated_at  = models.DateField(auto_now=True)

    class Meta:
        db_table = 'users'
