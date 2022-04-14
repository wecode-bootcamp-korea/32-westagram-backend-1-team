from django.db import models

class Users(models.Model):
    name = models.CharField(max_length=45)
    email = models.EmailField(max_length=300)
    password = models.CharField(max_length=300)
    phone_number = models.IntegerField()
