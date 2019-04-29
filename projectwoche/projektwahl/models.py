from django.db import models

class Projekt(models.Model):
    lehrer = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    grösse = models.IntegerField();

class Schueler(models.Model):
    name = models.CharField(max_length=100)
    projekt = models.ForeignKey(Projekt,on_delete=models.CASCADE)



# Create your models here.
