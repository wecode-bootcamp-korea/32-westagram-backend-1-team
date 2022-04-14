from django.db import models

class User(models.Model):
    name        = models.CharField(max_length=20)
    email       = models.EmailField(max_length=254)
    password    = models.CharField(max_length=20)
    phonenumber = models.IntegerField()

    class Meta:
        db_table = 'users'
