from django.db import models

class Users(models.Model):
    username = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    loggedin = models.BooleanField();
    def __str__(self):
        return self.username
# Create your models here.
